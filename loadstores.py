import mysql.connector
from mysql.connector import errorcode
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Database connection details
db_config = {
    'user': 'root',
    'password': 'Takomborerwa15!',
    'host': 'localhost',
    'database': 'stores'  # Ensure this matches your actual database
}

# Connect to MySQL
try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Generate and insert stores
    store_ids = []
    manager_ids = [fake.random_int(min=1, max=2000) for _ in range(2000)]  # Assume manager IDs
    for _ in range(2000):
        store_name = fake.company() + " Store"
        store_type = random.choice(['Physical', 'Online'])
        location = fake.address().replace("\n", ", ")
        opening_date = fake.date_between(start_date='-5y', end_date='today')

        query = ("INSERT INTO Stores (store_name, store_type, location, opening_date, manager_id) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (store_name, store_type, location, opening_date, random.choice(manager_ids))
        cursor.execute(query, data)
        store_ids.append(cursor.lastrowid)

    # Generate and insert inventory
    for _ in range(2000):
        store_id = random.choice(store_ids)
        product_id = fake.random_int(min=1, max=2000)  # Assumes existing product IDs
        quantity_available = random.randint(1, 500)
        last_updated = fake.date_this_year()

        query = ("INSERT INTO Inventory (store_id, product_id, quantity_available, last_updated) "
                 "VALUES (%s, %s, %s, %s)")
        data = (store_id, product_id, quantity_available, last_updated)
        cursor.execute(query, data)

    # Generate and insert sales
    for _ in range(2000):
        store_id = random.choice(store_ids)
        product_id = fake.random_int(min=1, max=2000)
        sale_date = fake.date_this_year()
        quantity_sold = random.randint(1, 100)
        total_sale_amount = round(quantity_sold * random.uniform(10, 100), 2)

        query = ("INSERT INTO Sales (store_id, product_id, sale_date, quantity_sold, total_sale_amount) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (store_id, product_id, sale_date, quantity_sold, total_sale_amount)
        cursor.execute(query, data)

    # Generate and insert store schedules
    for _ in range(2000):
        store_id = random.choice(store_ids)
        event_name = random.choice(['Grand Opening', 'Annual Sale', 'Maintenance Day', 'Weekend Promotion'])
        event_date = fake.date_between(start_date='-1y', end_date='+1y')
        event_type = random.choice(['Opening', 'Closing', 'Maintenance', 'Promotion'])

        query = ("INSERT INTO Store_Schedule (store_id, event_name, event_date, event_type) "
                 "VALUES (%s, %s, %s, %s)")
        data = (store_id, event_name, event_date, event_type)
        cursor.execute(query, data)

    # Commit the inserts
    cnx.commit()
    print("Data insertion completed successfully.")

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