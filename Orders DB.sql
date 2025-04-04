CREATE SCHEMA nikeorders;

USE nikeorders;

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    discount_id INT,
    payment_transaction_id INT NOT NULL,
    shipping_id INT NOT NULL,
    order_status_id INT NOT NULL
    -- FOREIGN KEY (user_id) REFERENCES Users(user_id),
    -- FOREIGN KEY (discount_id) REFERENCES Discounts(discount_id),
    -- FOREIGN KEY (payment_transaction_id) REFERENCES PaymentTransactions(payment_transaction_id),
	-- FOREIGN KEY (shipping_id) REFERENCES ShippingDetails(shipping_id),
    -- FOREIGN KEY (order_status_id) REFERENCES OrderStatuses(order_status_id)
);

-- Order Items Table
DROP TABLE IF EXISTS OrderItems;
CREATE TABLE OrderItems (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id VARCHAR(100),
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
    -- FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    -- FOREIGN KEY (product_id) REFERENCES Products(product_id)
);



-- Addresses Table
DROP TABLE IF EXISTS Addresses;
CREATE TABLE Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    address_type ENUM('billing', 'shipping') NOT NULL,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    phone_number VARCHAR(30)
    -- FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- Shipping Details Table
DROP TABLE IF EXISTS ShippingDetails;
CREATE TABLE ShippingDetails (
    shipping_id INT AUTO_INCREMENT PRIMARY KEY,
    address_id INT NOT NULL,
    order_id INT NOT NULL,
    shipping_method VARCHAR(100) NOT NULL,
    shipping_status ENUM('pending', 'in transit', 'delivered', 'returned') DEFAULT 'pending',
    tracking_number VARCHAR(50)
    -- FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);



-- Payment Transactions Table
DROP TABLE IF EXISTS PaymentTransactions;
CREATE TABLE PaymentTransactions (
    payment_transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method ENUM('credit card', 'debit card', 'paypal', 'gift card', 'voucher') NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME NOT NULL,
    transaction_reference VARCHAR(100) NOT NULL
);

-- Order Status Table
DROP TABLE IF EXISTS OrderStatus;
CREATE TABLE OrderStatus (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    status ENUM('pending', 'confirmed', 'shipped', 'delivered', 'cancelled','returned') NOT NULL,
    status_change_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    -- FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- Discounts Table
DROP TABLE IF EXISTS Discounts;
CREATE TABLE Discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    discount_code VARCHAR(50) NOT NULL,
    order_id INT NOT NULL,
    discount_type ENUM('percentage', 'fixed') NOT NULL,
    discount_value DECIMAL(10, 2) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL
);



