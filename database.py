import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "history.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        loc INTEGER,
        complexity INTEGER,
        coupling INTEGER,
        risk_score REAL,
        prediction TEXT,
        confidence INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_record(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history (
        filename, loc, complexity, coupling,
        risk_score, prediction, confidence
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["filename"],
        data["loc"],
        data["complexity"],
        data["coupling"],
        data["risk_score"],
        data["prediction"],
        data["confidence"]
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows