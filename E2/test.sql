INSERT INTO clinica (nome, telefone, morada) VALUES
('Clinica Lisboa', '213481226', 'Rua G, 1000-286 Lisboa');

INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES
('000000001', 'Medico 1', '210000021', 'Rua da Madalena, 1000-663 Lisboa', 'cardiologia'),
('000000002', 'Medico 2', '210000022', 'Rua dos Sapateiros, 1000-459 Lisboa', 'cardiologia');

INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES
('000000001', 'Clinica Lisboa', 0),
('000000002', 'Clinica Lisboa', 0),
('000000001', 'Clinica Lisboa', 1),
('000000002', 'Clinica Lisboa', 1),
('000000001', 'Clinica Lisboa', 2),
('000000002', 'Clinica Lisboa', 2),
('000000001', 'Clinica Lisboa', 3),
('000000002', 'Clinica Lisboa', 3),
('000000001', 'Clinica Lisboa', 4),
('000000002', 'Clinica Lisboa', 4),
('000000001', 'Clinica Lisboa', 5),
('000000002', 'Clinica Lisboa', 5),
('000000001', 'Clinica Lisboa', 6),
('000000002', 'Clinica Lisboa', 6);

INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES
('00601111112', '601111112', 'Paciente 601111112', '2107437962', 'Rua 601111112, 8734-112 Belém', '2000-09-20'),
('00601111113', '601111113', 'Paciente 601111113', '2103511141', 'Rua 601111113, 5580-179 Mouraria', '1968-06-23');

INSERT INTO consulta (id,ssn, nif, nome, data, hora, codigo_sns) VALUES
(1, '00601111112','000000001',  '2023-05-01', '09:00', ),
(2, '2023-05-01', '10:00', '000000002', '00601111112');

