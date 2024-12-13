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



--MIN
SELECT MIN(salario) AS salario_minimo
FROM empregados;

--Subconsulta com EXISTS
SELECT nome
FROM empregados e
WHERE EXISTS (
    SELECT 1
    FROM projetos p
    WHERE p.responsavel_id = e.id
);

--Uso de RANK
SELECT nome, salario,
       RANK() OVER (ORDER BY salario DESC) AS ranking
FROM empregados;

--Agrupamento e Soma
SELECT departamento_id, SUM(salario) AS total_salario
FROM empregados
GROUP BY departamento_id
ORDER BY total_salario DESC;


--  Inserção com Dados Novos
INSERT INTO empregados (nome, salario, departamento_id)
VALUES ('João', 3000, 1);



ALTER TABLE empregados
ADD COLUMN data_nascimento DATE;


-- Consulta com Inner Join e Filtros
SELECT e.nome, d.nome AS departamento, e.salario
FROM empregados e
INNER JOIN departamentos d ON e.departamento_id = d.id
WHERE e.salario > 4000;


-- Contagem de Funcionários por Departamento
SELECT d.nome AS departamento, COUNT(e.id) AS total_empregados
FROM departamentos d
LEFT JOIN empregados e ON d.id = e.departamento_id
GROUP BY d.nome;

-- Calculando Percentual
SELECT departamento_id, 
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM empregados) AS percentual
FROM empregados
GROUP BY departamento_id;


-- Uso de SUBSTRING
SELECT nome, SUBSTRING(nome, 1, 3) AS iniciais
FROM empregados;


--Filtragem com IN
SELECT nome
FROM empregados
WHERE departamento_id IN (1, 2, 3);


--Contagem com GROUP BY e HAVING
SELECT departamento_id, COUNT(*) AS total
FROM empregados
GROUP BY departamento_id
HAVING COUNT(*) > 5;

--Uso de INNER JOIN com Agregação
SELECT d.nome AS departamento, AVG(e.salario) AS media_salarial
FROM departamentos d
INNER JOIN empregados e ON d.id = e.departamento_id
GROUP BY d.nome;

--Filtro com NOT EXISTS
SELECT nome
FROM empregados e
WHERE NOT EXISTS (
    SELECT 1
    FROM projetos p
    WHERE p.responsavel_id = e.id
);


--Função de Janela com ROW_NUMBER
SELECT nome, salario,
       ROW_NUMBER() OVER (PARTITION BY departamento_id ORDER BY salario DESC) AS posicao
FROM empregados;


--Alterar Nome da Coluna
ALTER TABLE empregados
RENAME COLUMN antigo_nome TO novo_nome;


--Consulta com CROSS JOIN
SELECT e.nome, d.nome AS departamento
FROM empregados e
CROSS JOIN departamentos d;

--Atualização de Dados com Subconsulta

UPDATE empregados
SET salario = (SELECT AVG(salario) FROM empregados)
WHERE departamento_id = 2;


-- Consulta com CASE para Categorização
SELECT nome, 
       CASE 
           WHEN salario < 3000 THEN 'Baixo'
           WHEN salario BETWEEN 3000 AND 7000 THEN 'Médio'
           ELSE 'Alto'
       END AS faixa_salarial
FROM empregados;


-- Uso de TRIM para Remover Espaços
SELECT TRIM(nome) AS nome_limpo
FROM empregados;


--Inserindo Vários Registros
INSERT INTO empregados (nome, salario, departamento_id)
VALUES 
    ('Maria', 4000, 1),
    ('José', 4500, 2);


--Consulta de Múltiplas Tabelas com LEFT JOIN
SELECT e.nome, p.nome AS projeto
FROM empregados e
LEFT JOIN projetos p ON e.id = p.responsavel_id;


--Verificando Duplicados
SELECT nome, COUNT(*)
FROM empregados
GROUP BY nome
HAVING COUNT(*) > 1;

--Concatenação com Função de Agregação
SELECT departamento_id, GROUP_CONCAT(nome SEPARATOR ', ') AS empregados
FROM empregados
GROUP BY departamento_id;


--Remoção de Coluna
ALTER TABLE empregados
DROP COLUMN coluna_antiga;


--Consulta com Função de Agregação e Filtros
SELECT departamento_id, AVG(salario) AS media_salarial
FROM empregados
WHERE salario > 2500
GROUP BY departamento_id;

