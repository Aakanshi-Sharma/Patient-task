import sqlite3
import os

DB_PATH = 'database/patient.db'

def create_tables():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        username TEXT
    )
    """)


    conn.commit()
    conn.close()
    print("All tables created successfully.")

if __name__ == "__main__":
    create_tables()
