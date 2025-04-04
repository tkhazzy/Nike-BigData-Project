This folder contains all the necessary files, code, and data for setting up and populating the relational databases used in the project. The databases implemented are:

Users
Orders
Vendors
Employees
Stores
Contents:
SQL Files:

SQL scripts to create the databases and their respective tables. Each script is designed to ensure the schema adheres to 3NF for optimized database design and performance.
Generated Data:

For Users and Orders, data was generated using Apache Spark to simulate 1,000,000 rows for each table
The generated data is stored as Parquet files in the parquet/ directory. The Orders


For Vendors, Employees, and Stores, data was populated