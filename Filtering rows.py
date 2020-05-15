--- Filtering results
select title from films
where release_year > 2000;
>> films released  after the year 2000


--- Simple filtering of numeric values
select * from films
where release_year=2016;

select count(*) from films
where release_year<2000;

select title, release_year from films
where release_year>2000;


--- Simple filtering of text
select * from films
where language='French';

select name, birthdate from people
where birthdate='1974-11-11';

select count(language) from films
where language='Hindi';


select * from films
where certification='R';


--- WHERE AND
select title, release_year from films
where language='Spanish'
and release_year<2000;

select * from films
where language='Spanish'
and release_year>2000;

select * from films
where language='Spanish'
and release_year>2000
and release_year<2000;


--- WHERE AND OR
What does the OR operator do ?
>> Display only rows that meet at least one of the specified conditions.


--- WHERE AND OR(2)
select title, release_year from films
where release_year>1989
and release_year<2000;

select title, release_year from films
where (release_year>1989 and release_year<2000)
and (language='Spanish' or language='French');

select title, release_year from films
where (release_year>1989 and release_year<2000)
and (language='Spanish' or language='French')
and gross>2000000;



--- BETWEEN
what does the BETWEEN keywords do?
>> filter values in a specified range



--- BETWEEN(2)
select title, release_year from films
where release_year between 1990 and 2000;

select title, release_year from films
where release_year between 1990 and 2000
and budget>100000000;

select title, release_year from films
where release_year between 1990 and 2000
and language='Spanish'
and budget>100000000;

select title, release_year from films
where release_year between 1990 and 2000
and (language='Spanish' or language='French')
and budget>100000000;



--- WHERE IN
select title, release_year from films
where release_year in (1990, 2000)
and duartion>120;

select title, language from films
where language in ('English','Spanish','French');

select title, certification from films
where certifiaction in ('NC-17', 'R');



--- Introduction to NULL and IS NULL
WHAT DOES NULL REPRESENT ?
>> A missing value.



---  NULL and IS NULL
select name from people
where deathdate is null;

select title from films
where budget is null;

select count(films) from films
where language is null;



--- LIKE and NOT LIKE
select name from people
where name like 'B%';

select name from people
where name like '-r%';

select name from people
where name not like 'A%';

































