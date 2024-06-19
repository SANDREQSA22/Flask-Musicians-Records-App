import sqlite3

DATABASE2 = 'database2.db'

def init2_db():
    conn = sqlite3.connect(DATABASE2)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            musician_name TEXT NOT NULL,
            guitar_name TEXT NOT NULL,
            song_title TEXT NOT NULL,
            image_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init2_db()
