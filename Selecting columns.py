--- Onboarding | Tables
from looking at the tables, who is the first person listed in people table ?
>>  50 Cent


--- Onboarding | Query Result
who is the second person listed in the query result ?
>> A. Michael Baldwin


--- Onboarding | Errors
SELECT 'Datacamp <3 SQL'
AS result;


--- Onboarding | Bullet Exercises
SELECT 'SQL'
AS result;

SELECT 'SQL is'
AS result;

SELECT 'SQL is cool!'
AS result;

--- Beginning your SQL journey
how many fields does the employees table above contain ?
>> 4


--- SELECTing single columns
SELECT title FROM films;

SELECT release_year FROM films;

SELECT name FROM people;


--- SELECTing multiple columns
SELECT title FROM films;

SELECT title, release_year FROM films;

SELECT title, release_year, country FROM films;

SELECT * FROM films;


--- SELECT DISTINCT
SELECT DISTINCT country FROM films;

SELECT DISTINCT certification FROM films;

SELECT DISTINCT role FROM roles;


--- Learning COUNT
select count(*) from reviews;
>> 4,968


--- Practice with COUNT
SELECT COUNT(*) FROM people;

SELECT COUNT(birthdate) FROM people;

SELECT COUNT(DISTINCT birthdate) FROM people;

SELECT COUNT(DISTINCT language) FROM films;

SELECT COUNT(DISTINCT country) FROM films;



