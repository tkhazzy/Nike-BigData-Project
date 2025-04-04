-- Create STORES Schema
CREATE SCHEMA STORES;

-- Switch to STORES Schema
USE STORES;

-- Create Stores Table
CREATE TABLE Stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(255) NOT NULL,
    store_type ENUM('Physical', 'Online') NOT NULL,
    location VARCHAR(255),
    opening_date DATE,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES EmployeesDB1.Employees(employee_id) -- Reference Employees table from EmployeesDB1
);
-- Create Inventory Table
CREATE TABLE Inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT,
    product_id INT,
    quantity_available INT,
    last_updated DATE,
    FOREIGN KEY (store_id) REFERENCES Stores(store_id) -- Uncommented the foreign key

);

-- Create Sales Table
CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT,
    product_id INT,
    sale_date DATE,
    quantity_sold INT,
    total_sale_amount DECIMAL(10, 2),
    FOREIGN KEY (store_id) REFERENCES Stores(store_id) -- Uncommented the foreign key

);

-- Create Store_Schedule Table
CREATE TABLE Store_Schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT,
    event_name VARCHAR(255),
    event_date DATE,
    event_type ENUM('Opening', 'Closing', 'Maintenance', 'Promotion'),
    FOREIGN KEY (store_id) REFERENCES Stores(store_id) -- Uncommented the foreign key
);
