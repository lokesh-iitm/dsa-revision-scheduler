from .db import get_connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        topic TEXT,
        difficulty TEXT,
        solved_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS revisions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        problem_id INTEGER,
        revision_date TEXT,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()