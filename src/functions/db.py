import sqlite3

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    try:
        conn = sqlite3.connect('library.db')
        return conn
    except sqlite3.Error as error:
        print(f"Error while connecting to sqlite: {error}")
        return None

def create_database():
    """
    Creates the books table in the library database if it doesn't already exist.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS books
                            (id INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT,
                            password TEXT,
                            role TEXT)''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
