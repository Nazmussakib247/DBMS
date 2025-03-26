-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS railway_booking;

-- Use the database
USE railway_booking;

-- Users table to store user information
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trains table to store train information
CREATE TABLE IF NOT EXISTS trains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    destination VARCHAR(100) NOT NULL,
    train_name VARCHAR(100) NOT NULL,
    departure_time TIME,
    arrival_time TIME,
    fare DECIMAL(10,2),
    total_seats INT DEFAULT 100,
    available_seats INT DEFAULT 100
);

-- Bookings table to store ticket bookings
CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    train_id INT,
    passenger_name VARCHAR(100) NOT NULL,
    passenger_age INT NOT NULL,
    coach_type ENUM('AC', 'Non-AC', 'Sleeper') NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    journey_date DATE NOT NULL,
    status ENUM('Confirmed', 'Cancelled', 'Pending') DEFAULT 'Confirmed',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (train_id) REFERENCES trains(id) ON DELETE CASCADE
);

-- Payments table to store payment information
CREATE TABLE IF NOT EXISTS payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    amount DECIMAL(10,2) NOT NULL,
    payment_method ENUM('Credit Card', 'Debit Card', 'Net Banking', 'UPI', 'Wallet'),
    transaction_id VARCHAR(100),
    payment_status ENUM('Success', 'Failed', 'Pending') DEFAULT 'Pending',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE
);

-- Stations table (optional for extended functionality)
CREATE TABLE IF NOT EXISTS stations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    code VARCHAR(10) UNIQUE
);