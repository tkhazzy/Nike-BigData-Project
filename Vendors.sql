CREATE SCHEMA VENDORS;
USE VENDORS;

DROP TABLE IF EXISTS Vendors;
CREATE TABLE Vendors (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL,
    contact_name VARCHAR(255),
    contact_email VARCHAR(255) UNIQUE NOT NULL,
    contact_phone VARCHAR(50),
    location VARCHAR(255)
);





CREATE TABLE Products_Supplied (
    product_id INT,
    vendor_id INT,
    product_name VARCHAR(255),
    quantity_supplied INT,
    supply_date DATE,
    PRIMARY KEY (product_id, vendor_id),
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id)
);

CREATE TABLE Contracts (
    contract_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_id INT,
    start_date DATE,
    end_date DATE,
    payment_terms VARCHAR(255),
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id)
);


CREATE TABLE Shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_id INT,
    product_id INT,
    shipment_date DATE,
    quantity_shipped INT,
    delivery_status ENUM('Pending', 'Delivered', 'Delayed'),
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id),
    FOREIGN KEY (product_id) REFERENCES Products_Supplied(product_id)
);
