from fastapi import APIRouter
from datetime import datetime

from app.database.db import get_connection

router = APIRouter()


@router.get("/revisions/today")
def revisions_today():

    today = datetime.now().date().isoformat()

    conn = get_connection()
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
@router.get("/revisions/upcoming")
def upcoming_revisions():

    today = datetime.now().date().isoformat()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT r.id,
           p.title,
           p.topic,
           p.difficulty,
           r.revision_date
    FROM revisions r
    JOIN problems p
    ON p.id = r.problem_id
    WHERE r.revision_date > ?
    AND r.completed = 0
    ORDER BY r.revision_date
    """, (today,))

    rows = cursor.fetchall()

    conn.close()

    return rows
@router.get("/revisions/history")
def revision_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.title,
           p.topic,
           p.difficulty,
           r.revision_date,
           r.completed
    FROM revisions r
    JOIN problems p
    ON p.id = r.problem_id
    ORDER BY r.revision_date
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
@router.put("/revision/{revision_id}")
def complete_revision(revision_id: int):

    conn = get_connection()
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