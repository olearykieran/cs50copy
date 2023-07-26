-- Keep a log of any SQL queries you execute as you solve the mystery.

-- I ran this first query to get a better understanding of the format of the crime scene table
SELECT *
  FROM crime_scene_reports
 LIMIT 5

-- I then queried to find crime reports on that day at the correct location 7/28/2021
SELECT *
  FROM crime_scene_reports
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND street = "Humphrey Street";

-- Using info from crime scene reports check the 3 interviews from witnesses that day
SELECT *
  FROM interviews
 WHERE year = 2021
   AND month = 7
   AND day = 28;

-- Run security footage from paring lot of bakery within 10 minutes of theft (10:15 - 10:25) to find all cars
SELECT license_plate
  FROM bakery_security_logs
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND hour = 10
   AND minute BETWEEN 15 AND 25;
-- 5P2BI95
-- 94KL13X
-- 6P58WS2
-- 4328GD8
-- G412CB7
-- L93JTIZ
-- 322W7JE
-- 0NTHK55

-- Join with people to match license plates and find possible culprits
SELECT name
  FROM people
  JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
  WHERE year = 2021
   AND month = 7
   AND day = 28
   AND hour = 10
   AND minute BETWEEN 15 AND 25;
-- First suspects are:
-- Vaness
-- Bruce
-- Barry
-- Luca
-- Sofia
-- Iman
-- Diana
-- Kelsey

-- Check all atm withdrawals on Leggett Street
SELECT amount, account_number
  FROM atm_transactions
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND atm_location = "Leggett Street"
   AND transaction_type = "withdraw";

-- Find more Possible suspects via bank account number
SELECT people.name
  FROM people
  JOIN bank_accounts ON bank_accounts.person_id = people.id
  JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
  WHERE atm_transactions.year = 2021
   AND atm_transactions.month = 7
   AND atm_transactions.day = 28
   AND atm_transactions.atm_location = "Leggett Street"
   AND atm_transactions.transaction_type = "withdraw";
  -- Possible suspects are: Bruce, Diana, Iman & Luca



-- Check earliest flight out of fiftyville the next morning 7/29/2021
SELECT flights.id, destination_airport_id, origin_airport_id, hour, minute, flights.day
  FROM flights
  JOIN airports ON flights.origin_airport_id = airports.id
 WHERE flights.year = 2021
   AND flights.month = 7
   AND flights.day = 29
   AND airports.city = "Fiftyville"
   ORDER BY hour, minute;

-- Use the earliest flights destination id to figure out where the thief escaped to
SELECT city, full_name, abbreviation
  FROM airports
 WHERE id = 4;
-- LGA, NYC

-- CHeck the passengers on the flight to find passport id
SELECT passport_number
  FROM passengers
 WHERE flight_id = 36;


-- Find culprit using passport number
SELECT name
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = 36;
-- Luca & Bruce are left

-- Check phone calls to see if Luca or Bruce made a call that day
SELECT name
FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE phone_calls.year = 2021
AND phone_calls.day = 28
AND phone_calls.month = 7
AND phone_calls.duration < 60;
-- Bruce did it

-- See who Bruce called
SELECT phone_number
FROM people
WHERE name = "Bruce";

SELECT receiver
FROM phone_calls
WHERE caller = "(367) 555-5533"
AND phone_calls.year = 2021
AND phone_calls.day = 28
AND phone_calls.month = 7
AND phone_calls.duration < 60;

SELECT name
FROM people
WHERE phone_number = "(375) 555-8161";
-- He called Robin
