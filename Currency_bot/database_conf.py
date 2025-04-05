import sqlite3

def create_db():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices(
            name TEXT PRIMARY KEY,
            price TEXT,
            last_update TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

create_db()