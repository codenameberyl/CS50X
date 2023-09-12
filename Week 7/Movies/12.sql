-- list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.

WITH johnny_depp_movies_id AS (
  SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Johnny Depp')
),
helena_bonham_carter_movies_id AS (
  SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Helena Bonham Carter')
)

SELECT title FROM movies
WHERE id IN johnny_depp_movies_id AND id IN helena_bonham_carter_movies_id;