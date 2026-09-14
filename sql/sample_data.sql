SELECT *
FROM city_risk;

SELECT city 
FROM city_risk;

SELECT city
FROM city_risk
WHERE risk>= 0.7;

SELECT city
FROM city_risk
ORDER BY risk DESC
LIMIT 1;

SELECT risk_level, count(*)
FROM city_risk
GROUP BY risk_level;

SELECT city,risk_level  --单引号表示文本 双引号表示字段名
FROM city_risk
WHERE risk_level='低风险';

SELECT city 
FROM city_risk cr
ORDER BY risk ASC 
LIMIT 1;

SELECT AVG(risk)
FROM city_risk;

SELECT city ,risk
FROM city_risk
ORDER BY risk DESC 
LIMIT 2

SELECT city ,risk
FROM city_risk
WHERE risk > 0.6;

SELECT city
FROM city_risk
ORDER BY risk ASC 
LIMIT 2

SELECT city ,count(risk_level)
FROM city_risk
GROUP BY city;

SELECT MAX(risk)
FROM city_risk

SELECT risk_level,count(*)
FROM city_risk 
GROUP BY risk_level 
ORDER BY count DESC;

SELECT risk_level,
count(*) AS num
FROM city_risk 
GROUP BY risk_level
ORDER BY num DESC;

------------------------
SELECT city,risk_level
FROM city_risk;

SELECT city,risk
FROM city_risk
ORDER BY risk DESC 
LIMIT 1;

SELECT avg(risk) AS avg_risk
FROM city_risk;

SELECT risk_level, count(*) AS number
FROM city_risk
GROUP BY risk_level 
ORDER BY number DESC;

SELECT risk_level
WHERE city count()>1;

-------------------------
SELECT MAX(risk)
FROM city_risk;
 
SELECT min(risk)
FROM city_risk;

SELECT sum(risk)
FROM city_risk;

SELECT count(city)
FROM city_risk;

SELECT city, risk
FROM city_risk
ORDER BY risk DESC 
LIMIT 2
-------------------------

SELECT city
FROM city_risk;

SELECT city 
FROM city_risk
WHERE risk>=0.7;

SELECT AVG(risk) AS average_risk
FROM city_risk

SELECT city,risk
FROM city_risk
ORDER BY risk ASC 
LIMIT 2;

SELECT MAX(risk) AS "最高风险"
FROM city_risk;

----------------------------------
SELECT city 
FROM city_risk
WHERE risk_level = '高风险'

SELECT
	MAX(risk),
	MIN(risk)
FROM
	city_risk;
	-----------------------------------
CREATE TABLE city_population(
id SERIAL PRIMARY KEY,
city VARCHAR(50),
population INTEGER);

INSERT INTO city_population
(city,population)
VALUES 
('上海',24000000),
('南京',9500000),
('杭州',12000000),
('苏州',13000000),
('无锡',7000000);

SELECT *
FROM city_population;
-------------------------------
SELECT 
city_risk.city,
city_risk.risk,
city_population.population
FROM city_risk
INNER JOIN city_population
ON city_risk.city = city_population.city;
----------------------------------------------
SELECT city,population
FROM city_population;

SELECT city_risk.city,
city_risk.risk,
city_population.population
FROM city_risk
INNER JOIN city_population
ON city_risk.city = city_population.city;

SELECT city_risk.city,city_risk.risk,city_population.population
FROM city_risk
INNER JOIN city_population
ON city_risk.city=city_population.city
WHERE risk > 0.7;
-----------------------
SELECT r.city,r.risk,p.population
FROM city_risk AS r
INNER JOIN city_population AS p
ON r.city = p.city;

SELECT r.city ,r.risk,p.population
FROM city_risk AS r
INNER JOIN city_population AS p
ON r.city = p.city
WHERE population > 10000000

SELECT r.city, r.risk, p.population
FROM city_risk AS r 
INNER JOIN city_population AS p 
ON r.city = p.city 
ORDER BY risk DESC 
LIMIT 2;

SELECT r.city, r.risk,p.population
FROM city_risk AS r
INNER JOIN city_population as p 
ON r.city = p.city;



