import sqlite3

def init_db():
    conn = sqlite3.connect('hr.db')
    c = conn.cursor()
    
    # Leave requests
    c.execute('''CREATE TABLE IF NOT EXISTS leave_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    leave_type TEXT
                )''')
    
    # Onboarding
    c.execute('''CREATE TABLE IF NOT EXISTS onboarding (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    position TEXT,
                    start_date TEXT
                )''')
    
    # Exit
    c.execute('''CREATE TABLE IF NOT EXISTS exit_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    exit_date TEXT,
                    reason TEXT
                )''')

    conn.commit()
    conn.close()

def insert_leave(data):
    conn = sqlite3.connect('hr.db')
    c = conn.cursor()
    c.execute("INSERT INTO leave_requests (name, email, start_date, end_date, leave_type) VALUES (?, ?, ?, ?, ?)", 
              (data['name'], data['email'], data['start_date'], data['end_date'], data['leave_type']))
    conn.commit()
    conn.close()

def insert_onboarding(data):
    conn = sqlite3.connect('hr.db')
    c = conn.cursor()
    c.execute("INSERT INTO onboarding (name, email, position, start_date) VALUES (?, ?, ?, ?)", 
              (data['name'], data['email'], data['position'], data['start_date']))
    conn.commit()
    conn.close()

def insert_exit(data):
    conn = sqlite3.connect('hr.db')
    c = conn.cursor()
    c.execute("INSERT INTO exit_requests (name, email, exit_date, reason) VALUES (?, ?, ?, ?)", 
              (data['name'], data['email'], data['exit_date'], data['reason']))
    conn.commit()
    conn.close()
