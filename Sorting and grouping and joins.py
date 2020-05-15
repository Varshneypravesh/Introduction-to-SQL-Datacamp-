--- ORDER BY
How do you think ORDER BY sorts a column of text values by default ?
>> Alphabetically(A-Z)


--- Sorting single columns
select name from people
order by name;

select name from people
order by birthdate;

select name, birthdate from people
order by birthdate;


--- Sorting single columns (2)
select title from films
where release_year=2000 or release_year=2012
order by release_year;

select * from films
where release_year<>2015
order by duration;

select title, gross from films
where title like'M%'
order by title;


--- Sorting single columns(DESC)
select imdb_score, film_id from reviews
order by imdb_score desc;

select title from films
order by title desc;

select title, duration from films
order by duraion desc;


--- Sorting multiple columns
select birthdate, name from people
order by birthdate, name;

select release_year, duration, title from films
order by release_year, duration;

select certification, release_year, title from films
order by certification, release_year;

select name, birthdate from people
order by name, birthdate;


---- GROUP BY
What is GROUP BY used for ?
>> performing operation by group.


--- GROUP BY Practice
select release_year, count(*) from films
group by release_year;

select release_year, avg(duration) from films
group by release_year;

select release_year,max(budget)  from films
group by release_year;

select imdb_score, count(*) from reviews
group by imdb_score;


--- GROUP BY Practice(2)
select release_year, min(budget)  from films
group by release_year;

select language, sum(gross) from films
group by language;

select country, sum(budget) from films
group by country;

select release_year, country, max(budget)  from films
group by release_year, country
order by release_year, country;

select release_year, country, min(gross)  from films
group by release_year, country
order by release_year, country;


--- HAVING  a great time
select release_year from films
group by release_year
HAVING COUNT(title) > 200;


--- All together now
select release_year, budget, gross from films;

select release_year, budget, gross from films
where release_year>1990;

select release_year from films
group by release_year
having release_year>1990;

select release_year, avg(budget) as avg_budget, avg(gross) as avg_gross from films
group by release_year
having release_year > 1990

select release_year, avg(budget) as avg_budget, avg(gross) as avg_gross from films
where release_year>1990
group by release_year
having avg(budget)>60000000

select release_year, avg(budget) as avg_budget, avg(gross) as avg_gross from films
where release_year>1990
group by release_year
having avg(budget)>60000000
order by avg(gross) desc;


--- All together now(2)
select country, avg(budget) as avg_budget, avg(gross) as avg_gross from films
group by country
having count(title)>10
order by country
limit 5;


--- A taste of things to come
select title, imdb_score from films
join films
on films.id = reviews.film_id
where title = 'To kill a Mockingbird';

What is the IMDB score for the film to kill a Mockingbird ?
>> 8.4 




































