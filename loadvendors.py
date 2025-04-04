import mysql.connector
from mysql.connector import errorcode
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Database connection details
db_config = {
    'user': 'root',
    'password': 'Takomborerwa15!',
    'host': 'localhost',
    'database': 'vendors'
}

# Connect to MySQL
try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Generate and insert vendors
    vendor_ids = []
    for _ in range(2000):
        vendor_name = fake.company()
        contact_name = f"{fake.first_name()} {fake.last_name()}"
        contact_email = fake.unique.company_email()
        contact_phone = fake.phone_number()
        location = fake.address().replace("\n", ", ")

        query = ("INSERT INTO Vendors (vendor_name, contact_name, contact_email, contact_phone, location) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (vendor_name, contact_name, contact_email, contact_phone, location)
        cursor.execute(query, data)
        vendor_ids.append(cursor.lastrowid)

    # Generate and insert products supplied
    product_names = [fake.word() for _ in range(100)]
    for product_id in range(1, 2001):
        vendor_id = random.choice(vendor_ids)
        product_name = random.choice(product_names)
        quantity_supplied = random.randint(1, 1000)
        supply_date = fake.date_this_year().strftime("%Y-%m-%d")

        query = ("INSERT INTO Products_Supplied (product_id, vendor_id, product_name, quantity_supplied, supply_date) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (product_id, vendor_id, product_name, quantity_supplied, supply_date)
        cursor.execute(query, data)

    # Generate and insert contracts
    for _ in range(2000):
        vendor_id = random.choice(vendor_ids)
        start_date = fake.past_date(start_date="-2y").strftime("%Y-%m-%d")
        end_date = fake.future_date(end_date="+1y").strftime("%Y-%m-%d")
        payment_terms = random.choice(['Net 30', 'Net 45', 'Net 60', 'Due on receipt'])

        query = ("INSERT INTO Contracts (vendor_id, start_date, end_date, payment_terms) "
                 "VALUES (%s, %s, %s, %s)")
        data = (vendor_id, start_date, end_date, payment_terms)
        cursor.execute(query, data)

    # Generate and insert shipments
    for _ in range(2000):
        vendor_id = random.choice(vendor_ids)
        product_id = random.randint(1, 2000)
        shipment_date = fake.date_this_year().strftime("%Y-%m-%d")
        quantity_shipped = random.randint(1, 100)
        delivery_status = random.choice(['Pending', 'Delivered', 'Delayed'])

        query = ("INSERT INTO Shipments (vendor_id, product_id, shipment_date, quantity_shipped, delivery_status) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (vendor_id, product_id, shipment_date, quantity_shipped, delivery_status)
        cursor.execute(query, data)

    # Commit the inserts
    cnx.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if 'cnx' in locals() and cnx.is_connected():
        cursor.close()
        cnx.close()