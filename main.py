from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from datetime import datetime, timedelta

app = FastAPI(title="DSA Revision Scheduler")

DB_NAME = "scheduler.db"


# ---------------------
# DATABASE SETUP
# ---------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
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


init_db()


# ---------------------
# REQUEST MODEL
# ---------------------
class Problem(BaseModel):
    title: str
    topic: str
    difficulty: str


# ---------------------
# ADD PROBLEM
# ---------------------
@app.post("/problem")
def add_problem(problem: Problem):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    solved_date = datetime.now().date().isoformat()

    cursor.execute(
        """
        INSERT INTO problems(title, topic, difficulty, solved_date)
        VALUES(?,?,?,?)
        """,
        (
            problem.title,
            problem.topic,
            problem.difficulty,
            solved_date
        )
    )

    problem_id = cursor.lastrowid

    intervals = [1, 3, 7, 15, 30]

    for days in intervals:
        revision_date = (
            datetime.now() + timedelta(days=days)
        ).date().isoformat()

        cursor.execute(
            """
            INSERT INTO revisions(problem_id, revision_date)
            VALUES(?,?)
            """,
            (
                problem_id,
                revision_date
            )
        )

    conn.commit()
    conn.close()

    return {
        "message": "Problem added successfully",
        "problem_id": problem_id
    }


# ---------------------
# GET ALL PROBLEMS
# ---------------------
@app.get("/problems")
def get_problems():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    conn.close()

    return rows


# ---------------------
# TODAY'S REVISIONS
# ---------------------
@app.get("/revisions/today")
def revisions_today():

    today = datetime.now().date().isoformat()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.title,
           p.topic,
           p.difficulty,
           r.revision_date
    FROM revisions r
    JOIN problems p
    ON p.id = r.problem_id
    WHERE r.revision_date <= ?
    AND r.completed = 0
    """, (today,))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ---------------------
# COMPLETE REVISION
# ---------------------
@app.put("/revision/{revision_id}")
def complete_revision(revision_id: int):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE revisions
    SET completed = 1
    WHERE id = ?
    """, (revision_id,))

    conn.commit()
    conn.close()

    return {
        "message": "Revision completed"
    }


# ---------------------
# DASHBOARD
# ---------------------
@app.get("/dashboard")
def dashboard():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM problems"
    )
    total_problems = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM revisions
    WHERE completed = 0
    """)
    pending = cursor.fetchone()[0]

    conn.close()

    return {
        "total_solved_problems": total_problems,
        "pending_revisions": pending
    }