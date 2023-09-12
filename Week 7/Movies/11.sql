-- list the titles of the five highest rated movies (in order) that
-- Chadwick Boseman starred in, starting with the highest rated.

WITH highest_rated_movie_by_chadwick_boseman_id AS (
  SELECT movie_id FROM stars
  WHERE person_id = (SELECT id FROM people WHERE name = 'Chadwick Boseman')
)

SELECT title FROM movies
JOIN ratings
  ON movies.id = ratings.movie_id
WHERE id IN highest_rated_movie_by_chadwick_boseman_id ORDER BY rating DESC LIMIT 5;