import os
from logging.config import dictConfig

import psycopg
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row
from datetime import date, time

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
# Use the format postgres://username:password@hostname/database_name to connect to the database.
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
                FROM clinica;
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
            specialties = cur.execute(
                """
                SELECT DISTINCT especialidade
                FROM medico m, 
                    trabalha t, 
                    clinica c
                WHERE m.nif = t.nif AND t.nome = c.nome AND c.nome = %(clinica)s;
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
            doctors = cur.execute(
                """
                SELECT m.nome, c.data, c.hora
                FROM horario_disponivel c,
                    medico m,
                    JOIN trabalha t ON m.nif = t.nif
                    JOIN clinica cl ON t.nome = cl.nome
                    LEFT JOIN consulta co ON m.nif = co.nif
                WHERE c.nif = m.nif AND cl.nome = %(clinica)s AND m.especialidade = %(especialidade)s
                    AND  c.data >= CURRENT_DATE AND c.hora >= CURRENT_TIME 
                ORDER BY c.data, c.hora
                LIMIT 3;
                """,
                {"clinica": clinica, "especialidade": especialidade},
            ).fetchall()
            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(doctors)

@app.route("/a/<clinica>/registar/", methods=("POST",))
def register_appointment(clinica):
    """Registers an appointment in a clinic"""

    ssn = request.args.get("ssn")
    nif = request.args.get("nif")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = None

    if not ssn or not nif or not data or not hora:
        error = "Args missing."

    data_now = date.now()
    hora_now = time.now()

    if data_now > data or (data_now == data and hora_now > hora):
        error = "Invalid date or time."

    if error is not None:
        return error, 400
    
    else:
        with psycopg.connect(conninfo=DATABASE_URL) as conn:
            with conn.cursor(row_factory=namedtuple_row) as cur:
                cur.execute(
                    """
                    INSERT INTO consulta (nif, ssn, data, hora, clinica)
                    VALUES (%(nif)s, %(ssn)s, %(clinica)s, %(data)s, %(hora)s);
                    """,
                    {"nif": nif, "ssn": ssn, "data": data, "hora": hora, "clinica": clinica},
                )
            conn.commit()
        return jsonify({"message": "Appointment registered successfully"}), 200


@app.route("/a/<clinica>/cancelar/", methods=("POST",))
def cancel_appointment(clinica):
    """Cancels an appointment in a clinic"""

    ssn = request.args.get("ssn")
    nif = request.args.get("nif")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = None

    if not ssn or not nif or not data or not hora:
        error = "Args missing."

    data_now = date.now()
    hora_now = time.now()

    if data_now > data or (data_now == data and hora_now > hora):
        error = "Invalid date or time."

    if error is not None:
        return error, 400
    
    else:
        with psycopg.connect(conninfo=DATABASE_URL) as conn:
            with conn.cursor(row_factory=namedtuple_row) as cur:
                cur.execute(
                    """
                    DELETE FROM consulta
                    WHERE nif = %(nif)s AND ssn = %(ssn)s AND data = %(data)s AND hora = %(hora)s AND clinica = %(clinica)s;
                    """,
                    {"nif": nif, "ssn": ssn, "data": data, "hora": hora, "clinica": clinica},
                )
            conn.commit()
        return jsonify({"message": "Appointment canceled successfully"}), 200

if __name__ == "__main__":
    app.run()