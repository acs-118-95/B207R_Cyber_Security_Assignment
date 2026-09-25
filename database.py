import sqlite3

# Open the database or create it if it does not exist
db = sqlite3.connect("database/results.db")

# Creating a command tool to run SQL commands
command = db.cursor()

# Creating a table for storing the results
command.execute("""
CREATE TABLE IF NOT EXISTS prediction_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_text TEXT,
    prediction TEXT
)
""")

# Saving and Closing the database
db.commit()
db.close()

print("Database and table created successfully.")
