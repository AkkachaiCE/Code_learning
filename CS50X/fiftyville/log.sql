-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Theft tool place on July 28
-- Theft tool place on Humphrey Street

-- First scene report
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day =28
AND street = 'Humphrey Street';
-- >> at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery. |
--    Littering took place at 16:36. No known witnesses.
-- >> 3 persons may be thift (10:15 am)

--At bakery_security_logs from 10:15 to 10:25
SELECT activity, license_plate, hour, minute
FROM bakery_security_logs
WHERE year = 2021 AND month = 7
AND day = 28 AND hour = 10
AND minute >=15 AND minute <= 25;
-- >> There are 8 licens_plate at that time

--interviews information
SELECT name, transcript
FROM interviews
WHERE year = 2021 AND month = 7
AND day = 28;
-- | Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
--> exit parking in 10 minute, withdraw money at Leggett Street in the moring, earliest flight on 29

--Check the name of license_plate and calling with less than a minute
SELECT name, phone_calls.duration FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >=15 AND bakery_security_logs.minute <= 25
AND phone_calls.duration <= 60 AND phone_calls.year = 2021
AND phone_calls.month = 7 AND phone_calls.day = 28;


--ATM withdraw at Leggett Street (transaction)
SELECT account_number, amount
FROM atm_transactions
WHERE year = 2021 AND month = 7
AND day = 28 AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street';
-->

--Check license_plate, calling, withdraw money
SELECT name,phone_calls.receiver, phone_calls.duration FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
JOIN phone_calls ON people.phone_number = phone_calls.caller
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >=15 AND bakery_security_logs.minute <= 25
AND phone_calls.duration <= 60 AND phone_calls.year = 2021
AND phone_calls.month = 7 AND phone_calls.day = 28
AND atm_transactions.year = 2021 AND atm_transactions.month = 7
AND atm_transactions.day = 28    AND atm_transactions.transaction_type = 'withdraw'
AND atm_transactions.atm_location = 'Leggett Street';
--> Bruce, Diana

--Check license_plate, calling, withdraw money and flight, airport (may be first flight)
SELECT name, flights.hour, airports.city FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
JOIN phone_calls ON people.phone_number = phone_calls.caller
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON flights.destination_airport_id = airports.id
WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >=15 AND bakery_security_logs.minute <= 25
AND phone_calls.duration <= 60 AND phone_calls.year = 2021
AND phone_calls.month = 7 AND phone_calls.day = 28
AND atm_transactions.year = 2021 AND atm_transactions.month = 7
AND atm_transactions.day = 28    AND atm_transactions.transaction_type = 'withdraw'
AND atm_transactions.atm_location = 'Leggett Street'
AND flights.year = 2021 AND flights.month = 7
AND flights.day = 29;
--> Bruce | 8    | New York City with (375) 555-8161

--Check the flight 29 July 2021 (id 36)
SELECT origin_airport_id, destination_airport_id, FROM flights
WHERE year = 2021 AND month = 7 AND day = 29;

--Who is ACCOMPLICE
SELECT name, phone_number FROM people
WHERE phone_number = '(375) 555-8161';
--> Robin

--Check phone_calls from Robin
SELECT caller, receiver, duration
FROM phone_calls
WHERE year = 2021 AND month = 7
AND caller = '(375) 555-8161'
AND day = 28;


