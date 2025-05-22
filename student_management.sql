CREATE DATABASE student_management;

USE student_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(50),
    department VARCHAR(100),
    contact VARCHAR(15),
    email VARCHAR(100)
);
