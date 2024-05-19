import os
from logging.config import dictConfig

import psycopg
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row

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
                SELECT m.nome
                FROM medico m, 
                    trabalha t,
                    clinica c
                WHERE m.nif = t.nif AND t.nome = c.nome AND 
                    c.nome = %(clinica)s AND m.especialidade = %(especialidade)s;
                """,
                {"clinica": clinica}, {"especialidade": especialidade},
            ).fetchall()
            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(doctors)

@app.route("/a/<clinica>/registar/", methods=("POST",))
def register_appointment(clinica):
    """Registers an appointment in a clinic"""

    return jsonify({"status": "success"})


@app.route("/a/<clinica>/cancelar/", methods=("POST",))
def cancel_appointment(clinica):
    """Cancels an appointment in a clinic"""

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run()