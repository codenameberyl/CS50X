# Movies

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 7 - Movies Problem Set](https://cs50.harvard.edu/x/2023/psets/7/movies/). This lab involves writing SQL queries to extract information from a database of movies. The database contains data from IMDb about movies, including information about the movies themselves, the people who directed and starred in them, and their ratings.

## Getting Started

1. Download the files:

   ```bash
   cd movies
   ```

2. Navigate into the `movies` directory by typing `cd movies`.

## Implementation

You are provided with a SQLite database (`movies.db`) and a set of SQL query tasks to perform. The queries will help you extract specific information from the database. For each problem, create a `.sql` file with your solution.

## Solving the Problems

1. In `1.sql`, write a SQL query to list the titles of all movies released in 2008.

2. In `2.sql`, write a SQL query to determine the birth year of Emma Stone.

3. In `3.sql`, write a SQL query to list the titles of all movies with a release date on or after 2018, in alphabetical order.

4. In `4.sql`, write a SQL query to determine the number of movies with an IMDb rating of 10.0.

5. In `5.sql`, write a SQL query to list the titles and release years of all Harry Potter movies, in chronological order.

6. In `6.sql`, write a SQL query to determine the average rating of all movies released in 2012.

7. In `7.sql`, write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title.

8. In `8.sql`, write a SQL query to list the names of all people who starred in Toy Story.

9. In `9.sql`, write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.

10. In `10.sql`, write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.

11. In `11.sql`, write a SQL query to list the titles of the five highest-rated movies that Chadwick Boseman starred in, starting with the highest rated.

12. In `12.sql`, write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.

13. In `13.sql`, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

## Testing

You can test your SQL queries using the following command in the VS Code terminal:

```bash
cat filename.sql | sqlite3 movies.db
```

Replace `filename.sql` with the name of the SQL file containing your query.

## Hints

- Refer to the provided SQL keywords reference for syntax assistance.
- Maintain good style in your SQL queries, following the guidelines in `sqlstyle.guide`.

## Checking Results

To evaluate the correctness of your code, you can run your queries on the `movies.db` database using the `sqlite3` command in your terminal. You should find that executing each `.sql` file produces a result table with the expected number of columns and rows.