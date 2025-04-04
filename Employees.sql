-- Create Employees Database
CREATE DATABASE EmployeesDB;

-- Switch to Employees Database
USE EmployeesDB;

-- Create Employees Table (with role_id instead of job_title)
CREATE TABLE Employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    hire_date DATE,
    role_id INT,
    department_id INT,
    location VARCHAR(255),
    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
    -- Department will be added after Departments table creation
);

-- Create Roles Table
CREATE TABLE Roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(255) NOT NULL,
    description TEXT,
    min_salary DECIMAL(10, 2),
    max_salary DECIMAL(10, 2)
);

-- Create Departments Table
CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);

-- Create Payroll Table
CREATE TABLE Payroll (
    payroll_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    pay_period_start DATE,
    pay_period_end DATE,
    gross_salary DECIMAL(10, 2),
    tax_withheld DECIMAL(10, 2),
    net_salary DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- Create Performance Table
CREATE TABLE Performance (
    performance_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    review_date DATE,
    score INT CHECK (score BETWEEN 1 AND 10),
    comments TEXT,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
