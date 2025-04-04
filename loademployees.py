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
    'database': 'EmployeesDB'  # Ensure this matches your actual database
}

# Connect to MySQL
try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Generate Departments
    department_ids = []
    for _ in range(10):  # Assuming 10 departments for example
        department_name = fake.word().capitalize() + " Department"
        manager_id = None  # Assign manager later after generating employees

        query = ("INSERT INTO Departments (department_name, manager_id) "
                 "VALUES (%s, %s)")
        data = (department_name, manager_id)
        cursor.execute(query, data)
        department_ids.append(cursor.lastrowid)

    # Generate Employees
    employee_ids = []
    for _ in range(80000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        phone_number = fake.phone_number()[:20]  # Ensure within VARCHAR(20)
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        job_title = fake.job()
        department_id = random.choice(department_ids)
        salary = round(random.uniform(30000, 200000), 2)
        location = fake.address().replace("\n", ", ")

        query = ("INSERT INTO Employees (first_name, last_name, email, phone_number, hire_date, job_title, department_id, salary, location) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (first_name, last_name, email, phone_number, hire_date, job_title, department_id, salary, location)
        cursor.execute(query, data)
        employee_ids.append(cursor.lastrowid)

    # Assign managers to departments
    for dept_id in department_ids:
        manager_id = random.choice(employee_ids)
        query = "UPDATE Departments SET manager_id = %s WHERE department_id = %s"
        data = (manager_id, dept_id)
        cursor.execute(query, data)

    # Generate Roles
    for _ in range(100):  # Assuming 100 roles
        job_title = fake.job()
        description = fake.text(max_nb_chars=200)
        min_salary = round(random.uniform(30000, 70000), 2)
        max_salary = round(random.uniform(70000, 200000), 2)

        query = ("INSERT INTO Roles (job_title, description, min_salary, max_salary) "
                 "VALUES (%s, %s, %s, %s)")
        data = (job_title, description, min_salary, max_salary)
        cursor.execute(query, data)

    # Generate Payroll
    start_date = datetime(year=2022, month=1, day=1).date()
    end_date = datetime(year=2022, month=12, day=31).date()
    for emp_id in employee_ids[:1000]:  # Only for a subset to contain
        pay_period_start = fake.date_between(start_date=start_date, end_date=end_date)
        pay_period_end = fake.date_between(start_date=pay_period_start, end_date=end_date)
        gross_salary = round(random.uniform(1500, 5000), 2)
        tax_withheld = round(gross_salary * 0.2, 2)
        net_salary = gross_salary - tax_withheld

        query = ("INSERT INTO Payroll (employee_id, pay_period_start, pay_period_end, gross_salary, tax_withheld, net_salary) "
                 "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (emp_id, pay_period_start, pay_period_end, gross_salary, tax_withheld, net_salary)
        cursor.execute(query, data)

    # Generate Performance
    for emp_id in employee_ids[:1000]:  # Only for a subset
        review_date = fake.date_between(start_date='-2y', end_date='today')
        score = random.randint(1, 10)
        comments = fake.text(max_nb_chars=200)

        query = ("INSERT INTO Performance (employee_id, review_date, score, comments) "
                 "VALUES (%s, %s, %s, %s)")
        data = (emp_id, review_date, score, comments)
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