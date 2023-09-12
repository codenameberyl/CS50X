# Fiftyville

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 7 - Fiftyville Problem Set](https://cs50.harvard.edu/x/2023/psets/7/fiftyville/). In this lab, you are presented with a mystery in the town of Fiftyville where the CS50 Duck has been stolen. Your task is to identify the thief, the city they escaped to, and the identity of the accomplice who helped them escape. You are provided with a SQLite database called `fiftyville.db` that contains various tables of data related to the town's records. You need to use SQL queries to analyze the data and solve the mystery.

## Getting Started

1. Log into `cs50.dev` and open a terminal window.
2. Download the lab files by running the following commands in your terminal:

   ```bash
   cd Fiftyville
   ```

3. Navigate into the `Fiftyville` directory by typing `cd Fiftyville`.

## Solving the Mystery

Your task is to identify the thief, their escape city, and their accomplice. You will use SQL queries to extract information from the `fiftyville.db` database. Your thought process and the queries you execute will be logged in the `log.sql` file. Below are the steps you should follow to solve the mystery:

1. Start by examining the `crime_scene_reports` table to find information about the theft on July 28, 2021, on Humphrey Street.

2. Use the `interviews` table to gather information from the witnesses who were present at the time of the theft.

3. Investigate the ATM transactions on Leggett Street to gather clues about the thief's identity.

4. Analyze the bakery security logs to find license plate information related to the theft.

5. Use the information from the previous steps to identify the thief and the accomplice.

6. Determine the destination city where the thief escaped.

7. Use the `flights` table to find the flight taken by the thief to the escape city.

8. Analyze the `passengers` table to confirm the presence of the thief on the flight.

9. Use the accomplice's phone call records to identify the accomplice.

10. Complete the `answers.txt` file with the names of the thief, the escape city, and the accomplice.

## Testing

You can test your SQL queries using the following command in the VS Code terminal:

```bash
cat log.sql | sqlite3 fiftyville.db
```

```
+-----+
| id  |
+-----+
| 295 |
| 297 |
+-----+
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                       description                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+---------+
|  name   |
+---------+
| Ruth    |
| Eugene  |
| Raymond |
| Kiana   |
+---------+
+---------+
|  name   |
+---------+
| Ruth    |
| Eugene  |
| Raymond |
+---------+
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                         transcript                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                     transcript                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                     transcript                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+----------------+
| account_number |
+----------------+
| 28500762       |
| 28296815       |
| 76054385       |
| 49610011       |
| 16153065       |
| 25506511       |
| 81061156       |
| 26013199       |
+----------------+
+-----------+
| person_id |
+-----------+
| 467400    |
+-----------+
+-----------+
| person_id |
+-----------+
| 395717    |
+-----------+
+-----------+
| person_id |
+-----------+
| 449774    |
+-----------+
+-----------+
| person_id |
+-----------+
| 686048    |
+-----------+
+-----------+
| person_id |
+-----------+
| 458378    |
+-----------+
+-----------+
| person_id |
+-----------+
| 396669    |
+-----------+
+-----------+
| person_id |
+-----------+
| 438727    |
+-----------+
+-----------+
| person_id |
+-----------+
| 514354    |
+-----------+
+---------------+
| license_plate |
+---------------+
| 5P2BI95       |
| 94KL13X       |
| 6P58WS2       |
| 4328GD8       |
| G412CB7       |
| L93JTIZ       |
| 322W7JE       |
| 0NTHK55       |
+---------------+
+-------+
| name  |
+-------+
| Diana |
| Bruce |
+-------+
+--------+
|  name  |
+--------+
| Philip |
| Robin  |
+--------+
+-----------------------------+------------+
|          full_name          |    city    |
+-----------------------------+------------+
| Fiftyville Regional Airport | Fiftyville |
+-----------------------------+------------+
+-----------+-------------+
| min(hour) | min(minute) |
+-----------+-------------+
| 8         | 0           |
+-----------+-------------+
+-------------------+---------------+
|     full_name     |     city      |
+-------------------+---------------+
| LaGuardia Airport | New York City |
+-------------------+---------------+
+------------------------+
| destination_airport_id |
+------------------------+
| 4                      |
+------------------------+
+----+
| id |
+----+
| 36 |
+----+
+--------+
|  name  |
+--------+
| Kenny  |
| Sofia  |
| Taylor |
| Luca   |
| Kelsey |
| Edward |
| Bruce  |
| Doris  |
+--------+
+-------+
| name  |
+-------+
| Robin |
+-------+
```