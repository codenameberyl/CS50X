-- list the names of all people who have directed a movie that received a rating of at least 9.0.

WITH high_movie_ratings_id AS (
  SELECT movie_id FROM ratings WHERE rating >= 9.0
)

SELECT name FROM people
WHERE id IN (SELECT person_id FROM directors WHERE movie_id IN high_movie_ratings_id);