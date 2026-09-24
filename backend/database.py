import sqlite3

DB_PATH = "lobbystats.db"

def get_db():
    # check_same_thread=False allows FastAPI to handle concurrent requests without locking SQLite
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Returns database rows as dictionaries instead of raw tuples
    try:
        yield conn
    finally:
        conn.close()