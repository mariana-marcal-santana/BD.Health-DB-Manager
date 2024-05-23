DROP TABLE IF EXISTS clinica CASCADE;
DROP TABLE IF EXISTS enfermeiro CASCADE;
DROP TABLE IF EXISTS medico CASCADE;
DROP TABLE IF EXISTS trabalha CASCADE;
DROP TABLE IF EXISTS paciente CASCADE;
DROP TABLE IF EXISTS receita CASCADE;
DROP TABLE IF EXISTS consulta CASCADE;
DROP TABLE IF EXISTS consulta_auxiliar CASCADE;
DROP TABLE IF EXISTS observacao CASCADE;
DROP TABLE IF EXISTS horario_disponivel CASCADE;

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

CREATE TABLE consulta_auxiliar(
    id SERIAL PRIMARY KEY,
    ssn CHAR(11) NOT NULL REFERENCES paciente,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    codigo_sns CHAR(12) UNIQUE CHECK (codigo_sns ~ '^[0-9]+$'),
    UNIQUE(ssn, data, hora)
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

CREATE TABLE horario_disponivel(
    nif CHAR(9) NOT NULL REFERENCES medico,
    nome_clinica VARCHAR(80) NOT NULL REFERENCES clinica,
    especialidade VARCHAR(80) NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    PRIMARY KEY (nif, nome_clinica, especialidade, data, hora)
);


----------------------------------------
-- Restrictions and Triggers
----------------------------------------

CREATE OR REPLACE FUNCTION remove_horario_disponivel()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM horario_disponivel
    WHERE nif = NEW.nif
    AND nome_clinica = NEW.nome
    AND data = NEW.data
    AND hora = NEW.hora;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER remove_horario_trigger
AFTER INSERT ON consulta
FOR EACH ROW EXECUTE FUNCTION remove_horario_disponivel();


CREATE OR REPLACE FUNCTION check_medico_paciente()
RETURNS TRIGGER AS $$
DECLARE
    paciente_nif CHAR(9);
BEGIN
    -- Verificar se o paciente é um médico
    SELECT nif INTO paciente_nif FROM paciente WHERE ssn = NEW.ssn;

    -- Verificar se o NIF do médico é igual ao NIF do paciente
    IF paciente_nif = NEW.nif THEN
        RAISE EXCEPTION 'Um médico não pode consultar a si próprio ou a um paciente com o mesmo NIF';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER medico_paciente_trigger
BEFORE INSERT OR UPDATE ON consulta
FOR EACH ROW EXECUTE FUNCTION check_medico_paciente();

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
        RAISE NOTICE 'Tentativa de inserção: nif=%', NEW.nif;
        RAISE NOTICE 'Tentativa de inserção: nome=%', NEW.nome;
        RAISE NOTICE 'Tentativa de inserção: data=%', NEW.data;
        RAISE NOTICE 'Tentativa de inserção: dia_da_semana=%', EXTRACT(DOW FROM NEW.data);
        RAISE EXCEPTION 'Um médico só pode dar consultas na clínica em que trabalha no dia da semana correspondente à data da consulta';
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER medico_clinica_dia_trigger
BEFORE INSERT OR UPDATE ON consulta
FOR EACH ROW EXECUTE FUNCTION check_medico_clinica_dia();

