# Lab 7: Songs

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 7 - Lab 7: Songs](https://cs50.harvard.edu/x/2023/labs/7/). This lab involves writing SQL queries to extract information from a database of songs. The database contains data about songs and their artists from Spotify's top 100 streamed songs in 2018.

## Getting Started

1. Ensure you have SQLite installed on your system.
2. Download the lab files by running the following commands in your terminal:

   ```bash
   cd "Lab 7: Songs"
   ```

3. Navigate into the `songs` directory by typing `cd songs`.

## Implementation

You are provided with a SQLite database (`songs.db`) and a set of SQL query tasks to perform. The queries will help you extract specific information from the database. For each problem, create a `.sql` file with your solution.

## Solving the Problems

1. In `1.sql`, write a SQL query to list the names of all songs in the database.

2. In `2.sql`, write a SQL query to list the names of all songs in increasing order of tempo.

3. In `3.sql`, write a SQL query to list the names of the top 5 longest songs, in descending order of length.

4. In `4.sql`, write a SQL query that lists the names of any songs that have danceability, energy, and valence greater than 0.75.

5. In `5.sql`, write a SQL query that returns the average energy of all the songs.

6. In `6.sql`, write a SQL query that lists the names of songs that are by Post Malone.

7. In `7.sql`, write a SQL query that returns the average energy of songs that are by Drake.

8. In `8.sql`, write a SQL query that lists the names of the songs that feature other artists.

## Testing

You can test your SQL queries using the following command in the VS Code terminal:

```bash
cat filename.sql | sqlite3 songs.db
```

Replace `filename.sql` with the name of the SQL file containing your query.

## Spotify Wrapped Reflection

Reflect on how Spotify Wrapped calculates the "Audio Aura" for users based on the average energy, valence, and danceability of their top songs. Address the following questions in `answers.txt`:

- If `songs.db` contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
- Hypothesize why the way you've calculated this aura might not be very representative of the listener. What better ways of calculating this aura would you propose?