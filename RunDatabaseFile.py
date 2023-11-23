""" Click 'Run' to create Kicks Quest Database """

import sqlite3 as db
import csv
import json

# establish database and connection
conn = db.connect('KQBase.db')
# create cursor to execute sql commands
click = conn.cursor()


# create fresh start / delete table if present
click.execute('''DROP TABLE IF EXISTS customer''')

# create customer table
click.execute('''CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    email TEXT NOT NULL,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code INTEGER NOT NULL,
    birthdate DATE NOT NULL,
    payment REAL NOT NULL
)''')

# need to pull csv file for the values with which to create the table
with open(r'docs/customer.csv', 'r') as f:

    # need to hold values from csv being parsed
    customer_sheet = csv.DictReader(f)

    # need to iterate over csv and store each value respectively
    data_customer = [(i['customer_id'],
                      i['first'],
                      i['last'],
                      i['email'],
                      i['street'],
                      i['city'],
                      i['state'],
                      i['zip_code'],
                      i['birthdate'],
                      i['payment']) for i in customer_sheet]

# INSERT INTO customer table the column names and corresponding values per column
customer_insertion = '''INSERT INTO customer 
                        (customer_id, 
                        first, 
                        last, 
                        email, 
                        street, 
                        city, 
                        state, 
                        zip_code, 
                        birthdate, 
                        payment) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

# for sql to insert all data points parsed from the csv
click.executemany(customer_insertion, data_customer)
# save changes to the customer table
conn.commit()


# delete table if already present
click.execute('''DROP TABLE IF EXISTS delivery''')

# create delivery table in database
click.execute('''CREATE TABLE delivery (
    package TEXT,
    customer_id INTEGER PRIMARY KEY,
    ordered TIMESTAMP,
    delivered TIMESTAMP,
    payment TEXT,
    sold REAL,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    street TEXT NOT NULL,
    city TEXT,
    state TEXT, 
    zip_code INTEGER,
    design INTEGER
)''')

# use delivery csv to provide information held in a variable
# with statement automatically closes file
# written using somewhat pathlib syntax without lib install
with open(r'docs/delivery.csv', 'r') as file:
    delivery_sheet = csv.DictReader(file)
    data_delivery = [(i['package'],
                      i['customer_id'],
                      i['ordered'],
                      i['delivered'],
                      i['payment'],
                      i['sold'],
                      i['first'],
                      i['last'],
                      i['street'],
                      i['city'],
                      i['state'],
                      i['zip_code'],
                      i['design']) for i in delivery_sheet]

# insert delivery values to database
delivery_insertion = '''INSERT INTO delivery (package, 
                        customer_id, 
                        ordered, 
                        delivered, 
                        payment, 
                        sold, 
                        first, 
                        last, 
                        street, 
                        city, 
                        state, 
                        zip_code, 
                        design) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

# execute changes to database
click.executemany(delivery_insertion, data_delivery)
# save changes
conn.commit()


# delete table if already present
click.execute('''DROP TABLE IF EXISTS profit''')

# create profit table
click.execute('''CREATE TABLE profit (
    customer_id INTEGER,
    package TEXT,
    design INTEGER,
    sold REAL,
    payment TEXT,
    bought REAL, 
    sku INTEGER, 
    brand TEXT
)''')

# I need python to hold the values from the file
with open(r'docs/profit.json', 'r') as fj:
    profit_sheet = json.load(fj)
    data_profit = [(i['customer_id'],
                    i['package'],
                    i['design'],
                    i['sold'],
                    i['payment'],
                    i['bought'],
                    i['sku'],
                    i['brand']) for i in profit_sheet]

# hold value for insert statement for easier legibility
profit_insertion = '''INSERT OR IGNORE INTO profit(
                    customer_id, 
                    package, 
                    design, 
                    sold, 
                    payment, 
                    bought, 
                    sku, 
                    brand) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

# make and save changes
click.executemany(profit_insertion, data_profit)
conn.commit()

# must close database when done
conn.close()