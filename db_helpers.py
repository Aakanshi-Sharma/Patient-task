import sqlite3
import bcrypt

DB_PATH = 'database/patient.db'

conn=sqlite3.connect(DB_PATH)
def get_user_by_email(email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, password, username FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "email": row[1],
            "password": row[2],
            "username": row[3]
        }
    return None

def get_users_by_id(user_id):
    conn = sqlite3.connect('database/ecofinds.db')
    cursor = conn.cursor()

    cursor.execute("SELECT username, email FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_users():
    conn = sqlite3.connect('database/ecofinds.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1] , "sads":row[2]} for row in rows]

def create_user(email, username, raw_password):
    hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
    # hashed_password=raw_password
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password, username) VALUES (?, ?, ?)",
                       (email, hashed_password, username))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False
    
def delete_users(user_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id =?",
                       (user_id,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False
    
if __name__=="__main__":
    pass