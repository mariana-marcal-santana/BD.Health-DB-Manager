DROP TABLE IF EXISTS clinica CASCADE;
DROP TABLE IF EXISTS enfermeiro CASCADE;
DROP TABLE IF EXISTS medico CASCADE;
DROP TABLE IF EXISTS trabalha CASCADE;
DROP TABLE IF EXISTS paciente CASCADE;
DROP TABLE IF EXISTS receita CASCADE;
DROP TABLE IF EXISTS consulta CASCADE;
DROP TABLE IF EXISTS sintoma CASCADE;
DROP TABLE IF EXISTS observacao CASCADE;

----------------------------------------
-- Table Creation
----------------------------------------

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
dia_da_semana SMALLINT
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

----------------------------------------
-- Restrictions
----------------------------------------

CREATE OR REPLACE FUNCTION check_consulta_horario()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT (EXTRACT(MINUTE FROM NEW.horario) IN (0, 30) AND
           (EXTRACT(HOUR FROM NEW.horario) BETWEEN 8 AND 12 OR
            EXTRACT(HOUR FROM NEW.horario) BETWEEN 14 AND 18)) THEN
        RAISE EXCEPTION 'Horario da consulta inválido: %', NEW.horario;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_consulta_horario
BEFORE INSERT OR UPDATE ON consultas
FOR EACH ROW
EXECUTE FUNCTION check_consulta_horario();

CREATE OR REPLACE FUNCTION check_medico_nao_autoconsulta()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.medico_id = NEW.paciente_id THEN
        RAISE EXCEPTION 'Um médico não pode se consultar a si próprio.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_medico_nao_autoconsulta
BEFORE INSERT OR UPDATE ON consultas
FOR EACH ROW
EXECUTE FUNCTION check_medico_nao_autoconsulta();

CREATE TABLE horarios_medico (
    medico_id INT,
    clinica_id INT,
    dia_semana INT, -- 0: Domingo, 1: Segunda, ..., 6: Sábado
    PRIMARY KEY (medico_id, clinica_id, dia_semana)
);

CREATE OR REPLACE FUNCTION check_medico_clinica()
RETURNS TRIGGER AS $$
DECLARE
    v_count INT;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM horarios_medico
    WHERE medico_id = NEW.medico_id
    AND clinica_id = NEW.clinica_id
    AND dia_semana = EXTRACT(DOW FROM NEW.data);
    
    IF v_count = 0 THEN
        RAISE EXCEPTION 'Médico não trabalha nesta clínica neste dia da semana.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_medico_clinica
BEFORE INSERT OR UPDATE ON consultas
FOR EACH ROW
EXECUTE FUNCTION check_medico_clinica();


----------------------------------------
-- Injections
----------------------------------------

-- Inserir Clínicas
INSERT INTO clinica (nome, telefone, morada) VALUES
('Clinica A', '210000001', 'Rua A, 1000-100 Lisboa'),
('Clinica B', '210000002', 'Rua B, 1000-200 Lisboa'),
('Clinica C', '210000003', 'Rua C, 1000-300 Cascais'),
('Clinica D', '210000004', 'Rua D, 1000-400 Sintra'),
('Clinica E', '210000005', 'Rua E, 1000-500 Amadora');

-- Inserir Enfermeiros
INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES
('123456789', 'Enfermeiro A', '210000011', 'Rua F, 1000-600 Lisboa', 'Clinica A'),
('223456789', 'Enfermeiro B', '210000012', 'Rua G, 1000-700 Lisboa', 'Clinica B'),
('323456789', 'Enfermeiro C', '210000013', 'Rua H, 1000-800 Cascais', 'Clinica C'),
('423456789', 'Enfermeiro D', '210000014', 'Rua I, 1000-900 Sintra', 'Clinica D'),
('523456789', 'Enfermeiro E', '210000015', 'Rua J, 1000-000 Amadora', 'Clinica E'),
('623456789', 'Enfermeiro F', '210000016', 'Rua K, 1000-100 Lisboa', 'Clinica A'),
('723456789', 'Enfermeiro G', '210000017', 'Rua L, 1000-200 Lisboa', 'Clinica B'),
('823456789', 'Enfermeiro H', '210000018', 'Rua M, 1000-300 Cascais', 'Clinica C'),
('923456789', 'Enfermeiro I', '210000019', 'Rua N, 1000-400 Sintra', 'Clinica D'),
('023456789', 'Enfermeiro J', '210000020', 'Rua O, 1000-500 Amadora', 'Clinica E');

-- Inserir Médicos
INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES
('111111111', 'Medico 1', '210000021', 'Rua P, 1000-600 Lisboa', 'clinica geral'),
('211111111', 'Medico 2', '210000022', 'Rua Q, 1000-700 Lisboa', 'clinica geral'),
('311111111', 'Medico 3', '210000023', 'Rua R, 1000-800 Cascais', 'clinica geral'),
('411111111', 'Medico 4', '210000024', 'Rua S, 1000-900 Sintra', 'clinica geral'),
('511111111', 'Medico 5', '210000025', 'Rua T, 1000-000 Amadora', 'clinica geral'),
('611111111', 'Medico 6', '210000026', 'Rua U, 1000-100 Lisboa', 'clinica geral'),
('711111111', 'Medico 7', '210000027', 'Rua V, 1000-200 Lisboa', 'clinica geral'),
('811111111', 'Medico 8', '210000028', 'Rua W, 1000-300 Cascais', 'clinica geral'),
('911111111', 'Medico 9', '210000029', 'Rua X, 1000-400 Sintra', 'clinica geral'),
('011111111', 'Medico 10', '210000030', 'Rua Y, 1000-500 Amadora', 'clinica geral'),
('121212121', 'Medico 11', '210000031', 'Rua Z, 1000-600 Lisboa', 'ortopedia'),
('221212121', 'Medico 12', '210000032', 'Rua AA, 1000-700 Lisboa', 'ortopedia'),
('321212121', 'Medico 13', '210000033', 'Rua BB, 1000-800 Cascais', 'ortopedia'),
('421212121', 'Medico 14', '210000034', 'Rua CC, 1000-900 Sintra', 'cardiologia'),
('521212121', 'Medico 15', '210000035', 'Rua DD, 1000-000 Amadora', 'cardiologia'),
('621212121', 'Medico 16', '210000036', 'Rua EE, 1000-100 Lisboa', 'cardiologia'),
('721212121', 'Medico 17', '210000037', 'Rua FF, 1000-200 Lisboa', 'neurologia'),
('821212121', 'Medico 18', '210000038', 'Rua GG, 1000-300 Cascais', 'neurologia'),
('921212121', 'Medico 19', '210000039', 'Rua HH, 1000-400 Sintra', 'pediatria'),
('021212121', 'Medico 20', '210000040', 'Rua II, 1000-500 Amadora', 'pediatria');

-- Inserir Pacientes
DO $$
BEGIN
    FOR i IN 1..5000 LOOP
        INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES
        (LPAD(i::text, 11, '0'), LPAD((i + 5000)::text, 9, '0'), 'Paciente ' || i, '2100000' || LPAD(i::text, 4, '0'), 'Rua JJ, 1000-' || LPAD(i::text, 3, '0') || ' Lisboa', '1990-01-01'::DATE + (i % 365));
    END LOOP;
END $$;

-- Inserir Horários dos Médicos
INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES
('111111111', 'Clinica A', 1), ('111111111', 'Clinica B', 2), ('211111111', 'Clinica C', 3), 
('311111111', 'Clinica D', 4), ('411111111', 'Clinica E', 5), ('511111111', 'Clinica A', 6),
('611111111', 'Clinica B', 0), ('711111111', 'Clinica C', 1), ('811111111', 'Clinica D', 2),
('911111111', 'Clinica E', 3), ('011111111', 'Clinica A', 4), ('121212121', 'Clinica B', 5),
('221212121', 'Clinica C', 6), ('321212121', 'Clinica D', 0), ('421212121', 'Clinica E', 1),
('521212121', 'Clinica A', 2), ('621212121', 'Clinica B', 3), ('721212121', 'Clinica C', 4),
('821212121', 'Clinica D', 5), ('921212121', 'Clinica E', 6), ('021212121', 'Clinica A', 0);

-- Inserir Consultas
DO $$
DECLARE
    v_sns CHAR(11);
    v_nif CHAR(9);
    v_clinic VARCHAR(80);
    v_date DATE;
    v_time TIME;
BEGIN
    FOR i IN 1..20000 LOOP
        v_sns := LPAD((i % 5000 + 1)::text, 11, '0');
        v_nif := LPAD(((i % 20) + 1)::text, 9, '0');
        v_clinic := CASE 
                      WHEN i % 5 = 0 THEN 'Clinica A' 
                      WHEN i % 5 = 1 THEN 'Clinica B'
                      WHEN i % 5 = 2 THEN 'Clinica C'
                      WHEN i % 5 = 3 THEN 'Clinica D'
                      ELSE 'Clinica E' 
                    END;
        v_date := '2023-01-01'::DATE + (i % 365);
        v_time := TIME '08:00' + (i % 22) * INTERVAL '30 minutos';

        INSERT INTO consultation (ssn, nif, name, date, time, sns_code) VALUES
        (v_sns, v_nif, v_clinic, v_date, v_time, LPAD(i::text, 12, '0'));
    END LOOP;
END $$;
