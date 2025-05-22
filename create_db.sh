#!/bin/bash

# Set the path to your CSV file and database file
CSV_FILE="data/cpus.csv"
DB_FILE="database.sqlite"

# Check if the database already exists. If not, create a new one.
if [ ! -f "$DB_FILE" ]; then
  echo "Database not found. Creating a new one..."
  sqlite3 "$DB_FILE" "CREATE TABLE IF NOT EXISTS cpus (
  name TEXT NOT NULL,
  price REAL NOT NULL,
  clock REAL NOT NULL,
  cores INTEGER NOT NULL,
  rating REAL NOT NULL
);
"
else
  echo "Database exists. Proceeding with import..."
fi

# Import CSV into the cpus table
echo "Importing CSV into SQLite..."
sqlite3 "$DB_FILE" <<EOF
.mode csv
.import "$CSV_FILE" cpus
EOF

sqlite3 "$DB_FILE" "DELETE FROM cpus WHERE name='Name';"
# Select all data from the cpus table
echo "Selecting all data from the 'cpus' table..."
sqlite3 "$DB_FILE" "SELECT * FROM cpus;"
