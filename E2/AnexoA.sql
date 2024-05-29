DROP TABLE IF EXISTS clinica CASCADE;
DROP TABLE IF EXISTS enfermeiro CASCADE;
DROP TABLE IF EXISTS medico CASCADE;
DROP TABLE IF EXISTS trabalha CASCADE;
DROP TABLE IF EXISTS paciente CASCADE;
DROP TABLE IF EXISTS receita CASCADE;
DROP TABLE IF EXISTS consulta CASCADE;
DROP TABLE IF EXISTS observacao CASCADE;
DROP TABLE IF EXISTS horario_disponivel CASCADE;
DROP FUNCTION IF EXISTS validate_data_medico_paciente(VARCHAR, VARCHAR);
DROP FUNCTION IF EXISTS check_medico_clinica_dia();


CREATE TABLE clinica(
	nome VARCHAR(80) PRIMARY KEY,
	telefone VARCHAR(15) UNIQUE NOT NULL CHECK (telefone ~ '^[0-9]+$'),
	morada VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE enfermeiro(
	nif CHAR(9) PRIMARY KEY CHECK (nif ~ '^[0-9]+$'),
	nome VARCHAR(80) UNIQUE NOT NULL,
	telefone VARCHAR(15) NOT NULL CHECK (telefone ~ '^[0-9]+$'),
	morada VARCHAR(255) NOT NULL,
	nome_clinica VARCHAR(80) NOT NULL REFERENCES clinica (nome)
);

CREATE TABLE medico(
	nif CHAR(9) PRIMARY KEY CHECK (nif ~ '^[0-9]+$'),
	nome VARCHAR(80) UNIQUE NOT NULL,
	telefone VARCHAR(15) NOT NULL CHECK (telefone ~ '^[0-9]+$'),
	morada VARCHAR(255) NOT NULL,
	especialidade VARCHAR(80) NOT NULL
);

CREATE TABLE trabalha(
nif CHAR(9) NOT NULL REFERENCES medico,
nome VARCHAR(80) NOT NULL REFERENCES clinica,
dia_da_semana SMALLINT,
PRIMARY KEY (nif, dia_da_semana)
);

CREATE TABLE paciente(
	ssn CHAR(11) PRIMARY KEY CHECK (ssn ~ '^[0-9]+$'),
nif CHAR(9) UNIQUE NOT NULL CHECK (nif ~ '^[0-9]+$'),
	nome VARCHAR(80) NOT NULL,
	telefone VARCHAR(15) NOT NULL CHECK (telefone ~ '^[0-9]+$'),
	morada VARCHAR(255) NOT NULL,
	data_nasc DATE NOT NULL
);

CREATE TABLE consulta(
	id SERIAL PRIMARY KEY,
	ssn CHAR(11) NOT NULL REFERENCES paciente,
	nif CHAR(9) NOT NULL REFERENCES medico,
	nome VARCHAR(80) NOT NULL REFERENCES clinica,
	data DATE NOT NULL,
	hora TIME NOT NULL,
	codigo_sns CHAR(12) UNIQUE CHECK (codigo_sns ~ '^[0-9]+$'),
	UNIQUE(ssn, data, hora),
	UNIQUE(nif, data, hora)
);


CREATE TABLE horario_disponivel(
    data DATE,
    hora TIME
);

CREATE TABLE receita(
	codigo_sns VARCHAR(12) NOT NULL REFERENCES consulta (codigo_sns),
	medicamento VARCHAR(155) NOT NULL,
	quantidade SMALLINT NOT NULL CHECK (quantidade > 0),
	PRIMARY KEY (codigo_sns, medicamento)
);

CREATE TABLE observacao(
	id INTEGER NOT NULL REFERENCES consulta,
	parametro VARCHAR(155) NOT NULL,
	valor FLOAT,
PRIMARY KEY (id, parametro)
);

ALTER TABLE consulta
ADD CONSTRAINT check_horario_consulta
CHECK (
    hora >= '08:00:00' AND hora <= '18:30:00' 
    AND hora NOT IN ('13:00:00', '13:30:00')
    AND EXTRACT(MINUTE FROM hora) IN (0, 30)
    AND EXTRACT(SECOND FROM hora) = 0
);
CREATE OR REPLACE FUNCTION validate_data_medico_paciente(new_nif VARCHAR, new_ssn VARCHAR)
RETURNS BOOLEAN AS $$
DECLARE
    match_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO match_count
    FROM paciente p
    WHERE p.nif = new_nif AND p.ssn = new_ssn;

    RETURN match_count = 0;
END;
$$ LANGUAGE plpgsql;

ALTER TABLE consulta
ADD CONSTRAINT check_data_medico_paciente CHECK (
    validate_data_medico_paciente(nif, ssn)
);

CREATE OR REPLACE FUNCTION check_medico_clinica_dia()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM trabalha 
        WHERE nif = NEW.nif AND 
              nome = NEW.nome AND 
              dia_da_semana = EXTRACT(DOW FROM NEW.data)
    ) THEN
        -- O médico está programado para trabalhar nesta clínica neste dia da semana
        RETURN NEW;
    ELSE
        -- O médico não está programado para trabalhar nesta clínica neste dia da semana
        RAISE EXCEPTION 'Um médico só pode dar consultas na clínica em que trabalha no dia da semana correspondente à data da consulta';
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER medico_clinica_dia_trigger
BEFORE INSERT OR UPDATE ON consulta
FOR EACH ROW EXECUTE FUNCTION check_medico_clinica_dia();
