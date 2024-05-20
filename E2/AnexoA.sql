DROP TABLE IF EXISTS clinica CASCADE;
DROP TABLE IF EXISTS enfermeiro CASCADE;
DROP TABLE IF EXISTS medico CASCADE;
DROP TABLE IF EXISTS trabalha CASCADE;
DROP TABLE IF EXISTS paciente CASCADE;
DROP TABLE IF EXISTS receita CASCADE;
DROP TABLE IF EXISTS consulta CASCADE;
DROP TABLE IF EXISTS consulta_auxiliar CASCADE;
DROP TABLE IF EXISTS observacao CASCADE;
DROP TABLE IF EXISTS horarios_medico CASCADE;

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

----------------------------------------
-- Restrictions
----------------------------------------

CREATE OR REPLACE FUNCTION check_consulta_horario()
RETURNS TRIGGER AS $$
BEGIN
    IF (EXTRACT(MINUTE FROM NEW.hora) NOT IN (0, 30)) OR 
       (EXTRACT(HOUR FROM NEW.hora) NOT BETWEEN 8 AND 19) OR 
       (EXTRACT(HOUR FROM NEW.hora) = 13) THEN
        RAISE EXCEPTION 'Horário de consulta inválido. Deve ser à hora exata ou meia-hora no horário 8-13h e 14-19h';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER consulta_horario_trigger
BEFORE INSERT OR UPDATE ON consulta
FOR EACH ROW EXECUTE FUNCTION check_consulta_horario();


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
    IF NOT EXISTS (
        SELECT 1 FROM trabalha 
        WHERE nif = NEW.nif AND 
              nome = NEW.nome AND 
              dia_da_semana = EXTRACT(DOW FROM NEW.data)
    ) THEN
        RAISE EXCEPTION 'Um médico só pode dar consultas na clínica em que trabalha no dia da semana correspondente à data da consulta';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER medico_clinica_dia_trigger
BEFORE INSERT OR UPDATE ON consulta
FOR EACH ROW EXECUTE FUNCTION check_medico_clinica_dia();

----------------------------------------
-- Injections
----------------------------------------
-- Inserir Clínicas
INSERT INTO clinica (nome, telefone, morada) VALUES
('Clinica Lisboa A', '210000001', 'Rua A, 1000-100 Lisboa'),
('Clinica Lisboa B', '210000002', 'Rua B, 1000-200 Lisboa'),
('Clinica Oeiras A', '210000003', 'Rua C, 1000-300 Oeiras'),
('Clinica Cascais A', '210000004', 'Rua D, 1000-400 Cascais'),
('Clinica Sintra A', '210000005', 'Rua E, 1000-500 Sintra');

-- Inserir Enfermeiros
INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES
-- Enfermeiros para Clinica Lisboa A
('123456789', 'Enfermeiro A1', '210000011', 'Rua F, 1000-600 Lisboa', 'Clinica Lisboa A'),
('223456789', 'Enfermeiro A2', '210000012', 'Rua G, 1000-700 Lisboa', 'Clinica Lisboa A'),
('323456789', 'Enfermeiro A3', '210000013', 'Rua H, 1000-800 Lisboa', 'Clinica Lisboa A'),
('423456789', 'Enfermeiro A4', '210000014', 'Rua I, 1000-900 Lisboa', 'Clinica Lisboa A'),
('523456789', 'Enfermeiro A5', '210000015', 'Rua J, 1000-000 Lisboa', 'Clinica Lisboa A'),

-- Enfermeiros para Clinica Lisboa B
('623456789', 'Enfermeiro B1', '210000016', 'Rua K, 1000-100 Lisboa', 'Clinica Lisboa B'),
('723456789', 'Enfermeiro B2', '210000017', 'Rua L, 1000-200 Lisboa', 'Clinica Lisboa B'),
('823456789', 'Enfermeiro B3', '210000018', 'Rua M, 1000-300 Lisboa', 'Clinica Lisboa B'),
('923456789', 'Enfermeiro B4', '210000019', 'Rua N, 1000-400 Lisboa', 'Clinica Lisboa B'),
('023456789', 'Enfermeiro B5', '210000020', 'Rua O, 1000-500 Lisboa', 'Clinica Lisboa B'),

-- Enfermeiros para Clinica Oeiras A
('133456789', 'Enfermeiro C1', '210000021', 'Rua P, 1000-600 Oeiras', 'Clinica Oeiras A'),
('233456789', 'Enfermeiro C2', '210000022', 'Rua Q, 1000-700 Oeiras', 'Clinica Oeiras A'),
('333456789', 'Enfermeiro C3', '210000023', 'Rua R, 1000-800 Oeiras', 'Clinica Oeiras A'),
('433456789', 'Enfermeiro C4', '210000024', 'Rua S, 1000-900 Oeiras', 'Clinica Oeiras A'),
('533456789', 'Enfermeiro C5', '210000025', 'Rua T, 1000-000 Oeiras', 'Clinica Oeiras A'),

-- Enfermeiros para Clinica Cascais A
('633456789', 'Enfermeiro D1', '210000026', 'Rua U, 1000-100 Cascais', 'Clinica Cascais A'),
('733456789', 'Enfermeiro D2', '210000027', 'Rua V, 1000-200 Cascais', 'Clinica Cascais A'),
('833456789', 'Enfermeiro D3', '210000028', 'Rua W, 1000-300 Cascais', 'Clinica Cascais A'),
('933456789', 'Enfermeiro D4', '210000029', 'Rua X, 1000-400 Cascais', 'Clinica Cascais A'),
('033456789', 'Enfermeiro D5', '210000030', 'Rua Y, 1000-500 Cascais', 'Clinica Cascais A'),

-- Enfermeiros para Clinica Sintra A
('143456789', 'Enfermeiro E1', '210000031', 'Rua Z, 1000-600 Sintra', 'Clinica Sintra A'),
('243456789', 'Enfermeiro E2', '210000032', 'Rua AA, 1000-700 Sintra', 'Clinica Sintra A'),
('343456789', 'Enfermeiro E3', '210000033', 'Rua BB, 1000-800 Sintra', 'Clinica Sintra A'),
('443456789', 'Enfermeiro E4', '210000034', 'Rua CC, 1000-900 Sintra', 'Clinica Sintra A'),
('543456789', 'Enfermeiro E5', '210000035', 'Rua DD, 1000-000 Sintra', 'Clinica Sintra A');

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
('111111112', 'Medico 11', '210000031', 'Rua Z, 1000-600 Lisboa', 'clinica geral'),
('211111112', 'Medico 12', '210000032', 'Rua AA, 1000-700 Lisboa', 'clinica geral'),
('311111112', 'Medico 13', '210000033', 'Rua BB, 1000-800 Cascais', 'clinica geral'),
('411111112', 'Medico 14', '210000034', 'Rua CC, 1000-900 Sintra', 'clinica geral'),
('511111112', 'Medico 15', '210000035', 'Rua DD, 1000-000 Amadora', 'clinica geral'),
('611111112', 'Medico 16', '210000036', 'Rua EE, 1000-100 Lisboa', 'clinica geral'),
('711111112', 'Medico 17', '210000037', 'Rua FF, 1000-200 Lisboa', 'clinica geral'),
('811111112', 'Medico 18', '210000038', 'Rua GG, 1000-300 Cascais', 'clinica geral'),
('911111112', 'Medico 19', '210000039', 'Rua HH, 1000-400 Sintra', 'clinica geral'),
('011111112', 'Medico 20', '210000040', 'Rua II, 1000-500 Amadora', 'clinica geral'),
('121212121', 'Medico 21', '210000041', 'Rua JJ, 1000-600 Lisboa', 'ortopedia'),
('221212121', 'Medico 22', '210000042', 'Rua KK, 1000-700 Lisboa', 'ortopedia'),
('321212121', 'Medico 23', '210000043', 'Rua LL, 1000-800 Cascais', 'ortopedia'),
('421212121', 'Medico 24', '210000044', 'Rua MM, 1000-900 Sintra', 'cardiologia'),
('521212121', 'Medico 25', '210000045', 'Rua NN, 1000-000 Amadora', 'cardiologia'),
('621212121', 'Medico 26', '210000046', 'Rua OO, 1000-100 Lisboa', 'cardiologia'),
('721212121', 'Medico 27', '210000047', 'Rua PP, 1000-200 Lisboa', 'neurologia'),
('821212121', 'Medico 28', '210000048', 'Rua QQ, 1000-300 Cascais', 'neurologia'),
('921212121', 'Medico 29', '210000049', 'Rua RR, 1000-400 Sintra', 'pediatria'),
('021212121', 'Medico 30', '210000050', 'Rua SS, 1000-500 Amadora', 'pediatria'),
('131313131', 'Medico 31', '210000051', 'Rua TT, 1000-600 Lisboa', 'ortopedia'),
('231313131', 'Medico 32', '210000052', 'Rua UU, 1000-700 Lisboa', 'ortopedia'),
('331313131', 'Medico 33', '210000053', 'Rua VV, 1000-800 Cascais', 'ortopedia'),
('431313131', 'Medico 34', '210000054', 'Rua WW, 1000-900 Sintra', 'cardiologia'),
('531313131', 'Medico 35', '210000055', 'Rua XX, 1000-000 Amadora', 'cardiologia'),
('631313131', 'Medico 36', '210000056', 'Rua YY, 1000-100 Lisboa', 'cardiologia'),
('731313131', 'Medico 37', '210000057', 'Rua ZZ, 1000-200 Lisboa', 'neurologia'),
('831313131', 'Medico 38', '210000058', 'Rua AAA, 1000-300 Cascais', 'neurologia'),
('931313131', 'Medico 39', '210000059', 'Rua BBB, 1000-400 Sintra', 'pediatria'),
('031313131', 'Medico 40', '210000060', 'Rua CCC, 1000-500 Amadora', 'pediatria'),
('141414141', 'Medico 41', '210000061', 'Rua DDD, 1000-600 Lisboa', 'dermatologia'),
('241414141', 'Medico 42', '210000062', 'Rua EEE, 1000-700 Lisboa', 'dermatologia'),
('341414141', 'Medico 43', '210000063', 'Rua FFF, 1000-800 Cascais', 'dermatologia'),
('441414141', 'Medico 44', '210000064', 'Rua GGG, 1000-900 Sintra', 'dermatologia'),
('541414141', 'Medico 45', '210000065', 'Rua HHH, 1000-000 Amadora', 'dermatologia'),
('641414141', 'Medico 46', '210000066', 'Rua III, 1000-100 Lisboa', 'dermatologia'),
('741414141', 'Medico 47', '210000067', 'Rua JJJ, 1000-200 Lisboa', 'urologia'),
('841414141', 'Medico 48', '210000068', 'Rua KKK, 1000-300 Cascais', 'urologia'),
('941414141', 'Medico 49', '210000069', 'Rua LLL, 1000-400 Sintra', 'urologia'),
('041414141', 'Medico 50', '210000070', 'Rua MMM, 1000-500 Amadora', 'urologia'),
('151515151', 'Medico 51', '210000071', 'Rua NNN, 1000-600 Lisboa', 'urologia'),
('251515151', 'Medico 52', '210000072', 'Rua OOO, 1000-700 Lisboa', 'urologia'),
('351515151', 'Medico 53', '210000073', 'Rua PPP, 1000-800 Cascais', 'urologia'),
('451515151', 'Medico 54', '210000074', 'Rua QQQ, 1000-900 Sintra', 'urologia'),
('551515151', 'Medico 55', '210000075', 'Rua RRR, 1000-000 Amadora', 'urologia'),
('651515151', 'Medico 56', '210000076', 'Rua SSS, 1000-100 Lisboa', 'urologia'),
('751515151', 'Medico 57', '210000077', 'Rua TTT, 1000-200 Lisboa', 'urologia'),
('851515151', 'Medico 58', '210000078', 'Rua UUU, 1000-300 Cascais', 'urologia'),
('951515151', 'Medico 59', '210000079', 'Rua VVV, 1000-400 Sintra', 'urologia'),
('061515151', 'Medico 60', '210000080', 'Rua VVV, 1000-400 Sintra', 'urologia');

----------------------------------------
-- Functions to Injections
----------------------------------------
CREATE OR REPLACE FUNCTION inserir_trabalha()
RETURNS VOID AS
$$
DECLARE
    medico_nif CHAR(9);
    clinica_nome VARCHAR(80);
    dia_semana INTEGER;
BEGIN
    -- Atribuir cada médico a duas clínicas aleatórias, garantindo que não estejam alocados a mais de uma clínica no mesmo dia
    FOR medico_nif IN (SELECT nif FROM medico) LOOP
        FOR clinica_nome IN (
            SELECT nome
            FROM clinica 
            ORDER BY RANDOM() 
            LIMIT 2
        ) LOOP
            FOR dia_semana IN 0..6 LOOP
                -- Verificar se o médico já está alocado a uma clínica nesse dia
                IF NOT EXISTS (
                    SELECT 1
                    FROM trabalha
                    WHERE nif = medico_nif AND dia_da_semana = dia_semana
                ) THEN
                    INSERT INTO trabalha (nif, nome, dia_da_semana)
                    VALUES (medico_nif, clinica_nome, dia_semana);
                END IF;
            END LOOP;
        END LOOP;
    END LOOP;

    -- Loop para cada clínica
    FOR clinica_nome IN (SELECT nome FROM clinica) LOOP
        -- Loop para cada dia da semana
        FOR dia_semana IN 0..6 LOOP
            -- Selecionar aleatoriamente 8 médicos que ainda não estão trabalhando nesta clínica neste dia e não estão alocados a outra clínica neste dia
            FOR medico_nif IN (
                SELECT nif 
                FROM medico 
                WHERE nif NOT IN (
                    SELECT nif 
                    FROM trabalha 
                    WHERE dia_da_semana = dia_semana
                )
                ORDER BY RANDOM() 
                LIMIT 8
            ) LOOP
                -- Inserir na tabela trabalha
                INSERT INTO trabalha (nif, nome, dia_da_semana)
                VALUES (medico_nif, clinica_nome, dia_semana);
            END LOOP;
        END LOOP;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION inserir_pacientes()
RETURNS VOID AS $$
DECLARE
    contador INT;
    nome VARCHAR(80);
    morada VARCHAR(255);
    ssn CHAR(11);
    nif CHAR(9);
    telefone VARCHAR(15);
    data_nasc DATE;
    codigo_postal VARCHAR(8);
    localidade VARCHAR(255);
    localidades TEXT[] := ARRAY['Alfama', 'Baixa', 'Belém', 'Chiado', 'Graça', 'Mouraria', 'Parque das Nações', 'Restelo', 'Areeiro', 'Campo de Ourique'];
BEGIN
    contador := 1;

    WHILE contador <= 5000 LOOP
        nome := CONCAT('Paciente ', contador);
        
        -- Gerar código postal no formato XXXX-XXX
        codigo_postal := LPAD(FLOOR(RANDOM() * 10000)::TEXT, 4, '0') || '-' || LPAD(FLOOR(RANDOM() * 1000)::TEXT, 3, '0');
        
        -- Selecionar localidade aleatoriamente dentro de Lisboa
        localidade := localidades[FLOOR(RANDOM() * array_length(localidades, 1) + 1)];
        
        -- Construir a morada
        morada := CONCAT('Rua ', contador, ', ', codigo_postal, ' ', localidade);
        
        -- Gerar ssn e nif
        ssn := LPAD(contador::TEXT, 11, '0');
        nif := LPAD(contador::TEXT, 9, '0');
        
        -- Gerar telefone
        telefone := LPAD((9876543210 + contador)::TEXT, 15, '0');
        
        -- Gerar data de nascimento
        data_nasc := TO_DATE(FORMAT('%s-%s-%s', 
                                    1950 + (contador % 50), 
                                    LPAD(CEIL(RANDOM() * 12)::TEXT, 2, '0'), 
                                    LPAD(CEIL(RANDOM() * 28)::TEXT, 2, '0')
                                   ), 'YYYY-MM-DD');

        -- Inserir dados na tabela paciente
        INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc)
        VALUES (ssn, nif, nome, telefone, morada, data_nasc);

        contador := contador + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION inserir_consultas_auxiliares()
RETURNS VOID AS $$
DECLARE
    ssn_paciente CHAR(11);
    data_consulta DATE := '2023-01-01';
    hora_consulta TIME;
    consulta_id INT;
    total_pacientes INT;
    hora_base TIME;
    minuto_base INT;
BEGIN
    -- Obter o número total de pacientes
    SELECT COUNT(*) INTO total_pacientes FROM paciente;

    -- Gerar consultas para cada paciente
    FOR i IN 1..5000 LOOP
        -- Selecionar SSN do paciente, garantindo que não exceda o número total de pacientes
        SELECT ssn INTO ssn_paciente FROM paciente LIMIT 1 OFFSET (i - 1) % total_pacientes;

        -- Tentar gerar uma consulta única
        LOOP
            -- Gerar hora aleatória dentro dos intervalos especificados
            IF random() < 0.5 THEN
                hora_base := '08:00'::time + (floor(random() * 5) * INTERVAL '1 hour'); -- Entre 08:00 e 13:00
            ELSE
                hora_base := '14:00'::time + (floor(random() * 5) * INTERVAL '1 hour'); -- Entre 14:00 e 19:00
            END IF;

            -- Determinar se é hora exata ou meia-hora
            minuto_base := CASE WHEN random() < 0.5 THEN 0 ELSE 30 END;
            hora_consulta := hora_base + (minuto_base * INTERVAL '1 minute');

            -- Verificar se já existe uma consulta para o mesmo paciente na mesma data e hora
            PERFORM 1 FROM consulta_auxiliar WHERE ssn = ssn_paciente AND data = data_consulta AND hora = hora_consulta;
            IF NOT FOUND THEN
                -- Inserir consulta na tabela consulta_auxiliar
                INSERT INTO consulta_auxiliar (ssn, data, hora) VALUES (ssn_paciente, data_consulta, hora_consulta) RETURNING id INTO consulta_id;

                -- Atualizar código_sns com base no id gerado
                IF random() < 0.8 THEN
                    UPDATE consulta_auxiliar SET codigo_sns = LPAD(consulta_id::text, 12, '0') WHERE id = consulta_id;
                END IF;
                -- Sair do loop de tentativa
                EXIT;
            END IF;
        END LOOP;

        -- Incrementar a data_consulta
        data_consulta := data_consulta + INTERVAL '1 day';
        IF data_consulta > '2024-12-31' THEN
            data_consulta := '2023-01-01';
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION inserir_consultas()
RETURNS VOID AS $$
DECLARE
    consulta_aux RECORD;
    nif_medico CHAR(9);
    nome_clinica VARCHAR(80);
    total_medicos INT;
    total_clinicas INT;
    dia_da_semana_consulta INT;
BEGIN
    -- Obter o número total de médicos e clínicas
    SELECT COUNT(*) INTO total_medicos FROM medico;
    SELECT COUNT(*) INTO total_clinicas FROM clinica;

    -- Para cada consulta na tabela consulta_auxiliar
    FOR consulta_aux IN SELECT * FROM consulta_auxiliar ORDER BY data, hora LOOP
        -- Determinar o dia da semana da data da consulta (0 = domingo, 1 = segunda, ..., 6 = sábado)
        dia_da_semana_consulta := EXTRACT(DOW FROM consulta_aux.data);

        -- Selecionar um médico e uma clínica aleatoriamente, garantindo que as condições sejam atendidas
        LOOP
            -- Selecionar um médico aleatoriamente
            SELECT nif INTO nif_medico FROM medico OFFSET floor(random() * total_medicos) LIMIT 1;

            -- Selecionar uma clínica aleatoriamente onde o médico trabalha no dia da semana correspondente
            SELECT nome INTO nome_clinica
            FROM clinica
            WHERE nome IN (
                SELECT t.nome
                FROM trabalha t
                WHERE t.nif = nif_medico AND t.dia_da_semana = dia_da_semana_consulta
            )
            ORDER BY random()
            LIMIT 1;

            -- Verificar se o médico e a clínica selecionados atendem às condições
            IF nome_clinica IS NOT NULL THEN
                -- Verificar se o médico já tem consulta nesse horário
                PERFORM 1 FROM consulta WHERE nif = nif_medico AND data = consulta_aux.data AND hora = consulta_aux.hora;
                IF NOT FOUND THEN
                    -- Verificar se o médico já tem 2 consultas nesse dia
                    PERFORM 1 FROM consulta WHERE nif = nif_medico AND data = consulta_aux.data HAVING COUNT(*) < 2;
                    IF FOUND THEN
                        -- Verificar se a clínica já tem 20 consultas nesse dia
                        PERFORM 1 FROM consulta WHERE nome = nome_clinica AND data = consulta_aux.data HAVING COUNT(*) < 20;
                        IF FOUND THEN
                            -- Se as condições forem atendidas, sair do loop
                            EXIT;
                        END IF;
                    END IF;
                END IF;
            END IF;
        END LOOP;

        -- Inserir a consulta na tabela consulta
        INSERT INTO consulta (ssn, nif, nome, data, hora, codigo_sns)
        VALUES (consulta_aux.ssn, nif_medico, nome_clinica, consulta_aux.data, consulta_aux.hora, consulta_aux.codigo_sns);
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION inserir_receitas()
RETURNS VOID AS $$
DECLARE
    consulta RECORD;
    num_medicamentos INT;
    quantidade INT;
    medicamento_selecionado VARCHAR(155);
    medicamentos VARCHAR(155)[] := ARRAY['Medicamento 1', 'Medicamento 2', 'Medicamento 3', 'Medicamento 4', 'Medicamento 5', 'Medicamento 6'];
    total_consultas INT;
    consultas_com_receita INT;
BEGIN
    -- Obter o número total de consultas
    SELECT COUNT(*) INTO total_consultas FROM consulta;

    -- Para cada consulta na tabela consulta
    FOR consulta IN SELECT * FROM consulta WHERE codigo_sns IS NOT NULL ORDER BY random() LIMIT consultas_com_receita LOOP
        -- Selecionar aleatoriamente entre 1 e 6 medicamentos
        num_medicamentos := floor(random() * 6) + 1;

        FOR i IN 1..num_medicamentos LOOP
            -- Selecionar um medicamento aleatoriamente da lista
            medicamento_selecionado := medicamentos[floor(random() * array_length(medicamentos, 1)) + 1];

            -- Verificar se o medicamento já foi adicionado para a mesma consulta
            PERFORM 1 FROM receita WHERE codigo_sns = consulta.codigo_sns AND medicamento = medicamento_selecionado;
            IF NOT FOUND THEN
                -- Selecionar uma quantidade aleatoriamente entre 1 e 3
                quantidade := floor(random() * 3) + 1;

                -- Inserir a receita na tabela receita
                INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES (consulta.codigo_sns, medicamento_selecionado, quantidade);
            END IF;
        END LOOP;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION inserir_observacoes()
RETURNS VOID AS
$$
DECLARE
    consulta_id INTEGER;
    num_sintomas INTEGER;
    num_metricas INTEGER;
    parametro_sintoma VARCHAR(155);
    parametro_metrica VARCHAR(155);
    valor_metrica NUMERIC;
BEGIN
    -- Loop para cada consulta
    FOR consulta_id IN (SELECT id FROM consulta) LOOP
        -- Determinar aleatoriamente o número de observações de sintomas (entre 1 e 5)
        num_sintomas := FLOOR(RANDOM() * 5) + 1;
        
        -- Inserir observações de sintomas
        FOR i IN 1..num_sintomas LOOP
            -- Selecionar aleatoriamente um sintoma
            LOOP
                parametro_sintoma := (
                    SELECT parametro 
                    FROM (
                        VALUES 
                        ('Dor de cabeça'), ('Náusea'), ('Vómito'), ('Febre'), ('Tosse'),
                        ('Fadiga'), ('Falta de ar'), ('Tontura'), ('Perda de apetite'), ('Dor abdominal'),
                        ('Diarreia'), ('Constipação'), ('Dor no peito'), ('Dor nas articulações'), ('Dor muscular'),
                        ('Arrepios'), ('Suores noturnos'), ('Palpitações'), ('Confusão mental'), ('Visão turva'),
                        ('Zumbido nos ouvidos'), ('Formigamento'), ('Comichão'), ('Erupção cutânea'), ('Inchaço'),
                        ('Icterícia'), ('Tosse com sangue'), ('Dificuldade para engolir'), ('Rigidez matinal'),
                        ('Perda de peso inexplicável'), ('Incontinência urinária'), ('Urgência urinária'), ('Dores de garganta'),
                        ('Rouquidão'), ('Sonolência'), ('Alterações de humor'), ('Depressão'), ('Ansiedade'),
                        ('Insônia'), ('Pesadelos'), ('Paralisia'), ('Espasmos musculares'), ('Fraqueza'),
                        ('Tremores'), ('Sensação de desmaio'), ('Desmaios'), ('Dor na lombar'), ('Dor de dentes'),
                        ('Queimação ao urinar'), ('Alterações no paladar')
                    ) AS parametros(parametro)
                    ORDER BY RANDOM()
                    LIMIT 1
                );

                EXIT WHEN NOT EXISTS (
                    SELECT 1 
                    FROM observacao 
                    WHERE id = consulta_id 
                    AND parametro = parametro_sintoma
                );
            END LOOP;

            -- Inserir observação de sintoma
            INSERT INTO observacao (id, parametro)
            VALUES (consulta_id, parametro_sintoma);
        END LOOP;

        -- Determinar aleatoriamente o número de observações métricas (entre 0 e 3)
        num_metricas := FLOOR(RANDOM() * 4);

        -- Inserir observações métricas
        FOR i IN 1..num_metricas LOOP
            -- Selecionar aleatoriamente uma métrica
            LOOP
                parametro_metrica := (
                    SELECT parametro 
                    FROM (
                        VALUES 
                        ('Temperatura corporal'), ('Frequência cardíaca'), ('Pressão arterial sistólica'), ('Pressão arterial diastólica'), ('Saturação de oxigênio'),
                        ('Nível de glicose no sangue'), ('Peso corporal'), ('Altura'), ('Índice de massa corporal'), ('Taxa de respiração'),
                        ('Nível de colesterol total'), ('Nível de HDL'), ('Nível de LDL'), ('Nível de triglicerídeos'), ('Taxa de filtração glomerular'),
                        ('Volume urinário'), ('Taxa de sedimentação de eritrócitos'), ('Hemoglobina'), ('Contagem de leucócitos')
                    ) AS parametros(parametro)
                    ORDER BY RANDOM()
                    LIMIT 1
                );

                EXIT WHEN NOT EXISTS (
                    SELECT 1 
                    FROM observacao 
                    WHERE id = consulta_id 
                    AND parametro = parametro_metrica
                );
            END LOOP;

            -- Gerar valor aleatório para a métrica
            valor_metrica := RANDOM() * 100::NUMERIC;

            -- Inserir observação de métrica
            INSERT INTO observacao (id, parametro, valor)
            VALUES (consulta_id, parametro_metrica, valor_metrica);
        END LOOP;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION inserir_horario_disponivel() RETURNS VOID AS $$
DECLARE
    medico_nif CHAR(9);
    clinica_nome VARCHAR(80);
    especialidade_nome VARCHAR(80);
BEGIN
    FOR medico_nif, clinica_nome, especialidade_nome IN
        SELECT medico.nif, clinica.nome, medico.especialidade
        FROM medico
        JOIN trabalha ON medico.nif = trabalha.nif
        JOIN clinica ON trabalha.nome = clinica.nome
    LOOP
        INSERT INTO horario_disponivel (nif, dia_da_semana, data, hora, nome, especialidade)
        SELECT 
            medico_nif, 
            EXTRACT(DOW FROM datas.data), 
            datas.data, 
            horas.hora, 
            clinica_nome, 
            especialidade_nome
        FROM 
            (SELECT generate_series('2024-01-01'::date, '2024-12-31'::date, '1 day'::interval)::date AS data) AS datas,
            (SELECT ('08:00:00'::time + generate_series(0, (5 * 60 / 30) - 1) * '30 minutes'::interval)::time AS hora
             UNION ALL
             SELECT ('14:00:00'::time + generate_series(0, (5 * 60 / 30) - 1) * '30 minutes'::interval)::time AS hora) AS horas
        WHERE 
            EXTRACT(DOW FROM datas.data) BETWEEN 0 AND 6 AND
            NOT EXISTS (
                SELECT 1
                FROM consulta
                WHERE consulta.nif = medico_nif AND
                      consulta.data = datas.data AND
                      consulta.hora = horas.hora AND
                      consulta.nome = clinica_nome
            );
        ON CONFLICT (nif, dia_da_semana, data, hora) DO NOTHING;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT inserir_trabalha();
SELECT inserir_pacientes();
SELECT inserir_consultas_auxiliares();
SELECT inserir_consultas();
SELECT inserir_receitas();
SELECT inserir_observacoes();
SELECT inserir_horario_disponivel();    