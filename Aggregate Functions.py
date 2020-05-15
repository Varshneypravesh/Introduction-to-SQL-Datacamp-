--- Aggregate Functions
select sum(duration) from films;

select avg(duration) from films;

select min(duration) from films;

select max(duration) from films;


--- Aggregate Functions practice
select sum(gross) from films;

select avg(gross) from films;

select min(gross) from films;

select max(gross) from films;


--- Combining aggregate functions with WHERE
select sum(gross) from films
where release_year>=2000;

select avg(gross) from films
where title like 'A%';

select min(gross) from films
where release_year=1994;

select max(gross) from films
where release_year between 2000 and 2012;

--- A note on arithmetic
what is the result of SELECT(10 / 3); ?
>> 3


--- It 's AS simple AS aliasing
select title, gross-budget as net_profit
from films;

select title, duration/60.0 as duartion_hours
from films;

select avg(duration)/60.0 as avg_duration_hours
from films;


--- Even more aliasing
select count(deathdate)*100.0/count(*) as percentage_dead
from people;

select max(release_year)-min(release_year) as difference
from films;

select (max(release_year)-min(release_year))/10 as number_of_decades
from films;





































