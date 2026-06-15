from fastapi import APIRouter
from datetime import datetime, timedelta

from app.schemas.problem import Problem
from app.database.db import get_connection

router = APIRouter()


@router.post("/problem")
def add_problem(problem: Problem):

    conn = get_connection()
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
@router.get("/problems")
def get_problems():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    conn.close()

    return rows


@router.get("/dashboard")
def dashboard():

    conn = get_connection()
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
@router.get("/dashboard/topic-wise")
def topic_wise_dashboard():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT topic, COUNT(*)
    FROM problems
    GROUP BY topic
    """)

    rows = cursor.fetchall()

    conn.close()

    result = {}

    for topic, count in rows:
        result[topic] = count

    return result