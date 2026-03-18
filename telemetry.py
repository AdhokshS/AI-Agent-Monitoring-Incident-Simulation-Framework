import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("database/logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            response TEXT,
            confidence REAL,
            needs_escalation BOOLEAN,
            latency REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_event(user_input, response, confidence, needs_escalation, latency):
    conn = sqlite3.connect("database/logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO logs (user_input, response, confidence, needs_escalation, latency, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        user_input,
        response,
        confidence,
        needs_escalation,
        latency,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()