-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT id FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

-- FOUND report id = 295 and 297

SELECT description FROM crime_scene_reports WHERE id = 295;

-- FOUND crime description = Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

SELECT name FROM interviews WHERE transcript LIKE "%bakery%";

-- FOUND witness in interviews = Ruth, Eugene, Raymond, and Kiana

SELECT name FROM interviews WHERE transcript LIKE "%bakery%" AND year = 2021 AND month = 7 AND day = 28;

-- FOUND witness in interviews on 28/7/2021 = Ruth, Eugene, Raymond

SELECT transcript FROM interviews WHERE name = "Ruth" AND transcript LIKE "%bakery%";

-- FOUND Ruth said: "Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame."

SELECT transcript FROM interviews WHERE name = "Eugene" AND transcript LIKE "%bakery%";

-- FOUND Eugene said: "I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money."

SELECT transcript FROM interviews WHERE name = "Raymond" AND transcript LIKE "%bakery%";

-- FOUND Raymond said: "As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket."

-- CLUE
-- ATM at Leggett Street; --
-- Bakery Parking camera find footage from 10:15 to 10:25 am on 28/7/2021; --
-- the accomplice paid for flight ticket; ?
-- flight is earliest on 29/7/2021;
-- phone call was < 1 min; --

SELECT DISTINCT(account_number) FROM atm_transactions WHERE atm_location = "Leggett Street" AND year = 2021 AND month = 7 AND day = 28 AND transaction_type = "withdraw";

-- 28500762
-- 28296815
-- 76054385
-- 49610011
-- 16153065
-- 25506511
-- 81061156
-- 26013199

SELECT person_id FROM bank_accounts WHERE account_number = 28500762;
SELECT person_id FROM bank_accounts WHERE account_number = 28296815;
SELECT person_id FROM bank_accounts WHERE account_number = 76054385;
SELECT person_id FROM bank_accounts WHERE account_number = 49610011;
SELECT person_id FROM bank_accounts WHERE account_number = 16153065;
SELECT person_id FROM bank_accounts WHERE account_number = 25506511;
SELECT person_id FROM bank_accounts WHERE account_number = 81061156;
SELECT person_id FROM bank_accounts WHERE account_number = 26013199;

-- SUSPECTS ID
-- 467400
-- 395717
-- 449774
-- 686048
-- 458378
-- 396669
-- 438727
-- 514354

SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;

-- SUSPECTS LICENSE PLATE
-- 5P2BI95
-- 94KL13X
-- 6P58WS2
-- 4328GD8
-- G412CB7
-- L93JTIZ
-- 322W7JE
-- 0NTHK55

SELECT name FROM people WHERE (id = 467400
OR id = 395717
OR id = 449774
OR id = 686048
OR id = 458378
OR id = 396669
OR id = 438727
OR id = 514354)
AND (license_plate = '5P2BI95'
OR license_plate = '94KL13X'
OR license_plate = '6P58WS2'
OR license_plate = '4328GD8'
OR license_plate = 'G412CB7'
OR license_plate = 'L93JTIZ'
OR license_plate = '322W7JE'
OR license_plate = '0NTHK55')
AND phone_number in (SELECT caller FROM phone_calls WHERE duration < 60);

-- SUSPECTS (THIEF)
-- Diana
-- Bruce


SELECT name FROM people WHERE phone_number in
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller in
(SELECT phone_number FROM people WHERE name = "Diana" or name = "Bruce"));

-- SUSPECTS (ACCOMPLICE)
-- Philip
-- Robin

SELECT full_name, city FROM airports WHERE id in (SELECT origin_airport_id FROM flights WHERE year = 2021 AND month = 7 AND day = 29);

-- FOUND Fiftyville Regional Airport, Fiftyville flight id = 8

SELECT min(hour), min(minute) FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29;

-- FOUND earliest flight on 29/7/2021 = 8:00 am

SELECT full_name, city FROM airports WHERE id in
(SELECT destination_airport_id FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 AND hour = 8);

SELECT destination_airport_id FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 AND hour = 8;

SELECT id FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND destination_airport_id = 4;

-- FOUND LaGuardia Airport, New York City flight id = 36

SELECT name FROM people WHERE passport_number in (SELECT passport_number FROM passengers WHERE flight_id = 36);

-- Kenny
-- Sofia
-- Taylor
-- Luca
-- Kelsey
-- Edward
-- Bruce
-- Doris

-- FOUND suspect on flight = Bruce

-- FOUND thief escaped to New York City

SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND account_number in
(SELECT account_number FROM bank_accounts WHERE person_id in
(SELECT id FROM people WHERE name = 'Philip' OR name ='Robin'));

SELECT name FROM people WHERE phone_number in
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller in
(SELECT phone_number FROM people WHERE name = "Bruce"));

-- FOUND accomplice = Robin