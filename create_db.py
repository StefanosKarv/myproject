import sqlite3
import csv

# Connect to the SQLite3 database (or create it if it doesn't exist)
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Create a table (if not already created) to store CSV data
cursor.execute('''
CREATE TABLE IF NOT EXISTS motherboards (
    name TEXT,
    price REAL,
    rating REAL,
    socket TEXT,
    ramslots INTEGER
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS cpus (
    name TEXT,
    price REAL,
    clock REAL,
    cores INTEGER,
    rating INTEGER
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS gpus (
    name TEXT,
    price REAL,
    clock REAL,
    vram INTEGER,
    rating INTEGER
)
''')

# Function to read CSV and insert data into the database
def import_mobos(csv_file, conn, cursor):
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row (if there is one)

        for row in csv_reader:
            cursor.execute('''
            INSERT INTO motherboards (name, price, rating, socket, ramslots) 
            VALUES (?, ?, ?, ?, ?)
            ''', row)

    # Commit the changes and close the connection
    conn.commit()

def import_cpus(csv_file, conn, cursor):
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row (if there is one)

        for row in csv_reader:
            cursor.execute('''
            INSERT INTO cpus (name, price, clock, cores, rating) 
            VALUES (?, ?, ?, ?, ?)
            ''', row)

    # Commit the changes and close the connection
    conn.commit()

def import_gpus(csv_file, conn, cursor):
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row (if there is one)

        for row in csv_reader:
            cursor.execute('''
            INSERT INTO gpus (name, price, clock, vram, rating) 
            VALUES (?, ?, ?, ?, ?)
            ''', row)

    # Commit the changes and close the connection
    conn.commit()

# Import data from a CSV file to SQLite
csv_file = 'data/mobo.csv'  # Replace with your CSV file path
import_mobos(csv_file, conn, cursor)

# Import data from a CSV file to SQLite
csv_file = 'data/cpus.csv'  # Replace with your CSV file path
import_cpus(csv_file, conn, cursor)

# Import data from a CSV file to SQLite
csv_file = 'data/gpus.csv'  # Replace with your CSV file path
import_gpus(csv_file, conn, cursor)

# Close the database connection
conn.close()

print("Data imported successfully.")
