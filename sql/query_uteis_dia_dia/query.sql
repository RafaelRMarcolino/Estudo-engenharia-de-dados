SELECT e.nome, d.nome AS departamento
FROM empregados e
JOIN departamentos d ON e.departamento_id = d.id;


-- Uso de COALESCE retorna 'Não informado' ao inves de null
SELECT nome, COALESCE(telefone, 'Não informado') AS telefone
FROM empregados;


-- Atualização de Múltiplas Colunas
UPDATE empregados
SET salario = salario * 1.05, data_atualizacao = NOW()
WHERE departamento_id = 2;


-- Subconsulta em SELECT
SELECT  nome, salario from empregados
WHERE salario > (SELECT AVG(salario) FROM empregados);

-- CTE para Recursão
WITH RECURSIVE hierarquia AS (
    SELECT id, nome, generete_id
    FROM empregados
    WHERE generete_id IS NULL
    UNION ALL
    SELECT e.id, e.nome, e.gerente_id
    FROM empregados e
    INNER JOIN hierarquia h ON e.gerente_id = h.id
)
SELECT * FROM hierarquia;



-- left
SELECT e.nome, d.nome AS departamento
FROM empregados e
INNER JOIN departamentos d ON e.departamento_id = d.id;


-- Subconsulta em WHERE
SELECT nome 
FROM empregados
WHERE departamento_id IN (SELECT id FROM departamento WHERE nome = 'TI');



SELECT COUNT(*) AS total_empregados
FROM empregados;


-- Soma com GROUP BY
SELECT departamento_id, SUM(salario) AS total_salario
FROM empregados
GROUP BY departamento_id;


-- Filtragem com HAVING
SELECT departamento_id, AVG(salario) AS media_salarial
FROM empregados
GROUP BY departamento_id
HAVING AVG(salario) > 5000;


SELECT nome, salario
FROM empregados
ORDER BY salario DESC;

-- Subconsulta no SELECT
SELECT nome, (SELECT COUNT(*) FROM projetos WHERE responsavel_id = e.id) AS total_projetos
FROM empregados e;


-- Inserção com Select
INSERT INTO novos_empregados (nome, salario)
SELECT nome, salario FROM empregados WHERE data_admissao > '2023-01-01';


-- Atualização Condicional
UPDATE empregados
SET salario = salario * 1.1
WHERE departamento_id = 3;

-- Remoção com Condição
DELETE FROM empregados
WHERE salario < 2000;



-- Concatenação de Strings
SELECT CONCAT(nome, ' - ', salario) AS empregado_info
FROM empregados;

-- Filtragem com LIKE
SELECT nome
FROM empregados
WHERE nome LIKE 'A%';

-- LIMIT
SELECT nome, salario
FROM empregados
ORDER BY salario DESC
LIMIT 10;

-- Uso de BETWEEN
SELECT nome
FROM empregados
WHERE salario BETWEEN 3000 AND 7000;


-- Count com Agrupamento
SELECT departamento_id, COUNT(*) AS total
FROM empregados
GROUP BY departamento_id;


-- Atualização Baseada em Subconsulta
UPDATE empregados
SET salario = salario * 1.2
WHERE id IN (SELECT id FROM novos_empregados);

