-- base de dados auxiliar para testar a 5.2
INSERT INTO clinica (nome, telefone, morada) VALUES
('Clinica Lisboa', '213481226', 'Rua G, 1000-286 Lisboa');

INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES
('000000001', 'Medico 1', '210000021', 'Rua da Madalena, 1000-663 Lisboa', 'cardiologia');

INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES
('000000001', 'Clinica Lisboa', 0),
('000000001', 'Clinica Lisboa', 1),
('000000001', 'Clinica Lisboa', 2),
('000000001', 'Clinica Lisboa', 3),
('000000001', 'Clinica Lisboa', 4),
('000000001', 'Clinica Lisboa', 5),
('000000001', 'Clinica Lisboa', 6);

INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES
('00601111112', '601111112', 'Paciente 601111112', '2107437962', 'Rua 601111112, 8734-112 Belém', '2000-09-20');

INSERT INTO consulta (id,ssn, nif, nome, data, hora, codigo_sns) VALUES
('1', '00601111112','000000001', 'Clinica Lisboa', '2023-05-01', '09:00', '024598217681'),
('2', '00601111112','000000001', 'Clinica Lisboa', '2023-06-01', '09:00', '199834669724'),
('3', '00601111112','000000001', 'Clinica Lisboa', '2023-07-01', '09:00', '997276712647'),
('4', '00601111112','000000001', 'Clinica Lisboa', '2023-08-01', '09:00', '796103997589'),
('5', '00601111112','000000001', 'Clinica Lisboa', '2023-09-01', '09:00', '437102383413'),
('6', '00601111112','000000001', 'Clinica Lisboa', '2023-10-01', '09:00', '054294000434'),
('7', '00601111112','000000001', 'Clinica Lisboa', '2023-11-01', '09:00', '375745669349'),
('8', '00601111112','000000001', 'Clinica Lisboa', '2023-12-01', '09:00', '961003265031'),
('9', '00601111112','000000001', 'Clinica Lisboa', '2024-01-01', '09:00', '945929392948'),
('10', '00601111112','000000001', 'Clinica Lisboa','2024-02-01', '09:00', '028034170366'),
('11', '00601111112','000000001', 'Clinica Lisboa','2024-03-01', '09:00', '668783151172'),
('12', '00601111112','000000001', 'Clinica Lisboa','2024-04-01', '09:00', '917309312645'),
('13', '00601111112','000000001', 'Clinica Lisboa','2024-05-01', '09:00', '445444067937'),
('14', '00601111112','000000001', 'Clinica Lisboa','2024-06-01', '09:00', '645540484079');

INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES
('024598217681', 'medicamento 1', 1),
('199834669724', 'medicamento 1', 2),
('997276712647', 'medicamento 1', 3),
('796103997589', 'medicamento 1', 4),
('437102383413', 'medicamento 1', 5),
('054294000434', 'medicamento 1', 6),
('375745669349', 'medicamento 1', 7),
('961003265031', 'medicamento 1', 8),
('945929392948', 'medicamento 1', 9),
('028034170366', 'medicamento 1', 10),
('668783151172', 'medicamento 1', 11),
('917309312645', 'medicamento 1', 12),
('445444067937', 'medicamento 1', 13),
('645540484079', 'medicamento 1', 14);
