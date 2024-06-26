import os
from logging.config import dictConfig

import psycopg
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row
from datetime import date, time, datetime

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
# postgres://username:password@hostname/database_name to connect to the database.
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://saude:saude@postgres/saude")

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s:%(lineno)s - %(funcName)20s(): %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.config.from_prefixed_env()
log = app.logger

@app.route("/", methods=("GET",))
def all_clinics():
    """Shows all clinics in DB - name and address"""
    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            clinics = cur.execute(
                """
                SELECT nome, morada
                FROM clinica
                ORDER BY nome;
                """,
                {},
            ).fetchall()
            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(clinics)

@app.route("/c/<clinica>/", methods=("GET",))
def clinics_specialty(clinica):
    """Shows all specialties in a clinic"""
    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            cur.execute(
                """
                SELECT nome FROM clinica WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica},
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Clinic not found.", "status": "error"}), 404
            specialties = cur.execute(
                """
                SELECT DISTINCT especialidade
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                JOIN clinica c ON t.nome = c.nome
                WHERE c.nome = %(clinica)s;
                """,
                {"clinica": clinica},
            ).fetchall()
            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(specialties)

@app.route("/c/<clinica>/<especialidade>/", methods=("GET",))
def clinics_doctors_slots(clinica, especialidade):
    """Shows all doctors in a clinic with a specific specialty and the first 3 available appointment slots"""
    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            cur.execute(
                """
                SELECT nome FROM clinica WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica},
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Clinic not found.", "status": "error"}), 404
            cur.execute(
                """
                SELECT c.nome
                FROM clinica c
                JOIN trabalha t ON t.nome = c.nome
                JOIN medico m ON m.nif = t.nif
                WHERE m.especialidade = %(especialidade)s AND c.nome = %(clinica)s;
                """,
                {"clinica": clinica, "especialidade": especialidade}
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Specialty not found in clinic.", "status": "error"}), 404
            cur.execute(
                """
                SELECT DISTINCT m.nif, m.nome
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                JOIN clinica cl ON cl.nome = t.nome
                WHERE cl.nome = %(clinica)s AND m.especialidade = %(especialidade)s
                ORDER BY m.nome
                """,
                {"clinica": clinica, "especialidade": especialidade},
            )
            info = []
            for row in cur.fetchall():
                nif, nome = row[0], row[1]
                cur.execute("""SET TIMEZONE = 'Europe/Lisbon';""")
                appointments = cur.execute(
                    """ 
                    WITH consultas_medico AS (
                        SELECT data, hora
                        FROM consulta
                        WHERE nif = %(nif)s
                    )
                    SELECT h.data, h.hora
                    FROM horario_disponivel h
                    JOIN trabalha t ON t.dia_da_semana = EXTRACT(DOW FROM h.data)
                    LEFT JOIN consultas_medico c ON c.data = h.data AND c.hora = h.hora
                    WHERE c.data IS NULL AND (h.data > CURRENT_DATE OR 
                    (h.data = CURRENT_DATE AND h.hora > CURRENT_TIME))
                    GROUP BY h.data, h.hora
                    ORDER BY h.data, h.hora
                    LIMIT 3;
                    """,
                    {"nif": nif},
                ).fetchall()
                log.debug(f"Found {cur.rowcount} rows.")
         
                def process_row(row):
                    return { "data": row[0].isoformat() if row[0] else None,
                        "hora": row[1].strftime('%H:%M:%S') if row[1] else None }
                
                info_medico = [process_row(row) for row in appointments]
                info_medico.insert(0, nome)

                info += info_medico

    return jsonify(info)

@app.route("/a/<clinica>/registar/", methods=("POST",))
def register_appointment(clinica):
    """Registers an appointment in a clinic"""

    ssn = request.args.get("ssn")
    nif = request.args.get("nif")
    data = request.args.get("data")
    hora = request.args.get("hora")

    if not ssn or not nif or not data or not hora:
        return jsonify({"message": "Missing arguments.", "status": "error"}), 400

    data_now = date.today().strftime("%Y-%m-%d")
    hora_now = datetime.now().time().strftime("%H:%M:%S")

    hora_time = datetime.strptime(hora, "%H:%M:%S")

    if data_now > data or (data_now == data and hora_now > hora) or\
        hora_time.hour < 8 or hora_time.hour == 13 or hora_time.hour > 18 or\
        (hora_time.minute != 0 and hora_time.minute != 30) or hora_time.second != 0:
        return jsonify({"message": "Invalid date or time.", "status": "error"}), 400

    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            cur.execute("""SELECT * FROM consulta FOR UPDATE;""")
            cur.execute(
                """
                SELECT nome FROM clinica WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica},
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Clinic not found.", "status": "error"}), 404
            cur.execute(
                """
                SELECT nome FROM paciente WHERE ssn = %(ssn)s;
                """,
                {"ssn": ssn}
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Patient not found.", "status": "error"}), 400
            cur.execute(
                """
                SELECT nome FROM medico WHERE nif = %(nif)s;
                """,
                {"nif": nif}
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Doctor not found.", "status": "error"}), 400
            cur.execute(
                """
                SELECT * FROM paciente
                WHERE nif = %(nif)s AND ssn = %(ssn)s;
                """,
                {"nif": nif, "ssn": ssn}
            )
            if cur.fetchone() is not None:
                return jsonify({"message": "Doctor and patient can't be the same person.", "status": "error"}), 400
            cur.execute(
                """
                SELECT * FROM trabalha 
                WHERE nif = %(nif)s AND nome = %(clinica)s AND 
                      dia_da_semana = EXTRACT(DOW FROM %(data)s::DATE);
                """,
                {"nif": nif, "clinica": clinica, "data":data}
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Doctor doesn't work in the clinic in this day.", "status": "error"}), 400
            cur.execute(
                """
                SELECT id FROM consulta
                WHERE (nif = %(nif)s AND data = %(data)s AND hora = %(hora)s) OR
                    (ssn = %(ssn)s AND data = %(data)s AND hora = %(hora)s);
                """,
                {"nif": nif, "ssn": ssn, "data": data, "hora": hora},
            )
            if cur.fetchone() is not None:
                return jsonify({"message": "Either doctor or patient already have an appointment.", "status": "error"}), 400
            cur.execute(
                """
                SELECT id + 1 AS last_id FROM consulta ORDER BY id DESC LIMIT 1;
                """
            )
            last_id = cur.fetchone()
            if last_id is None: last_id = 1
            else: last_id = last_id.last_id
            cur.execute(
                """
                INSERT INTO consulta (id, nif, ssn, nome, data, hora, codigo_sns)
                VALUES (%(last_id)s, %(nif)s, %(ssn)s, %(clinica)s, %(data)s, %(hora)s, NULL);
                """,
                {"last_id": last_id, "nif": nif, "ssn": ssn, "data": data, "hora": hora, "clinica": clinica},
            )

    return jsonify({"message": "Appointment registered successfully"}), 200

@app.route("/a/<clinica>/cancelar/", methods=("DELETE", "POST",))
def cancel_appointment(clinica):
    """Cancels an appointment in a clinic"""

    ssn = request.args.get("ssn")
    nif = request.args.get("nif")
    data = request.args.get("data")
    hora = request.args.get("hora")

    if not ssn or not nif or not data or not hora:
        return jsonify({"message": "Missing arguments.", "status": "error"}), 400

    data_now = date.today().strftime("%Y-%m-%d")
    hora_now = datetime.now().time().strftime("%H:%M:%S")

    hora_time = datetime.strptime(hora, "%H:%M:%S")

    if data_now > data or (data_now == data and hora_now > hora) or\
        hora_time.hour < 8 or hora_time.hour == 13 or hora_time.hour > 18 or\
        (hora_time.minute != 0 and hora_time.minute != 30) or hora_time.second != 0:
        return jsonify({"message": "Invalid date or time.", "status": "error"}), 400

    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            cur.execute("""SELECT * FROM consulta FOR UPDATE;""")
            cur.execute(
                """
                SELECT nome FROM clinica WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica},
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Clinic not found.", "status": "error"}), 404
            cur.execute(
                """
                SELECT nome FROM paciente WHERE ssn = %(ssn)s;
                """,
                {"ssn": ssn}
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Patient not found.", "status": "error"}), 400
            cur.execute(
                """
                SELECT nome FROM medico WHERE nif = %(nif)s;
                """,
                {"nif": nif},
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Doctor not found.", "status": "error"}), 400
            cur.execute(
                """
                SELECT id FROM consulta 
                WHERE nif = %(nif)s AND ssn = %(ssn)s AND data = %(data)s AND hora = %(hora)s AND nome = %(clinica)s;
                """,
                {"nif": nif, "ssn": ssn, "data": data, "hora": hora, "clinica": clinica},
            )
            if cur.fetchone() is None:
                return jsonify({"message": "Appointment not found.", "status": "error"}), 400
            cur.execute(
                """
                DELETE FROM consulta
                WHERE nif = %(nif)s AND ssn = %(ssn)s AND data = %(data)s AND hora = %(hora)s AND nome = %(clinica)s;
                """,
                {"nif": nif, "ssn": ssn, "data": data, "hora": hora, "clinica": clinica},
            )

    return jsonify({"message": "Appointment canceled successfully"}), 200


if __name__ == "__main__":
    app.run()