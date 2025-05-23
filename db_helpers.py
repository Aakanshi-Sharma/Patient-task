import sqlite3
import bcrypt

DB_PATH = 'database/patient.db'


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_user_by_email(email):
    conn = get_db_connection()
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
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT username, email FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1] , "sads":row[2]} for row in rows]

def create_user(email, username, raw_password):
    hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
    try:
        conn = get_db_connection()
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
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id =?",
                       (user_id,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False
    
# -----PATIENT-------------------

def create_patient(name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date):
    conn = get_db_connection()
    conn.execute(
        '''
        INSERT INTO patient 
        (name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date)
    )
    conn.commit()
    conn.close()


def get_patient_data():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patient').fetchall()
    conn.close()
    return patients

def get_patient_by_id(patient_id):
    conn = get_db_connection()
    patient = conn.execute(
        'SELECT * FROM patient WHERE id = ?',
        (patient_id,)
    ).fetchone()
    conn.close()
    return patient
def update_patient(patient_id, name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date):
    conn = get_db_connection()
    conn.execute(
        '''
        UPDATE patient 
        SET name = ?, age = ?, address = ?, phone = ?, email = ?, disease = ?, 
            current_condition = ?, doctor = ?, admit_date = ?, discharge_date = ?
        WHERE id = ?
        ''',
        (name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date, patient_id)
    )
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM patient WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()


if __name__=="__main__":
    create_patient("abc1", 48, "test", "0000000000","test@gmail.com","Lung disease", "Improving","Dr. ABC","22-05-2025", "" )
    # print(get_patient_data())
    pass