CREATE MATERIALIZED VIEW historial_paciente AS
--Observacao
SELECT
    c.id,
    c.ssn,
    c.nif,
    c.nome,
    c.data,
    EXTRACT(YEAR FROM c.data) AS ano,
    EXTRACT(MONTH FROM c.data) AS mes,
    EXTRACT(DAY FROM c.data) AS dia_do_mes,
    TO_CHAR(c.data, 'Day') AS dia_da_semana,
    SUBSTRING(cl.morada FROM '[0-9]{4}-[0-9]{3} (.*)') AS localidade
    --EXTRACT(DOW FROM c.data) AS dia_da_semana,
    --cl.morada AS localidade, com SUBSTRING
    m.especialidade,
    'observacao' AS tipo,
    o.parametro AS chave,
    o.valor AS valor
FROM
    consulta c
JOIN
    clinica cl ON c.nome = cl.nome
JOIN
    medico m ON c.nif = m.nif
JOIN
    observacao o ON c.id = o.id
UNION ALL
--Receita
SELECT
    c.id,
    c.ssn,
    c.nif,
    c.nome,
    c.data,
    EXTRACT(YEAR FROM c.data) AS ano,
    EXTRACT(MONTH FROM c.data) AS mes,
    EXTRACT(DAY FROM c.data) AS dia_do_mes,
    TO_CHAR(c.data, 'Day') AS dia_da_semana,
    SUBSTRING(cl.morada FROM '[0-9]{4}-[0-9]{3} (.*)') AS localidade
    --EXTRACT(DOW FROM c.data) AS dia_da_semana,
    --cl.morada AS localidade, com SUBSTRING
    m.especialidade,
    'receita' AS tipo,
    r.medicamento AS chave,
    r.quantidade AS valor
FROM
    consulta c
JOIN
    clinica cl ON c.nome = cl.nome
JOIN
    medico m ON c.nif = m.nif
JOIN
    receita r ON c.codigo_sns = r.codigo_sns;
