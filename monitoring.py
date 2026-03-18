import sqlite3


def fetch_recent_logs(limit=5):
    conn = sqlite3.connect("database/logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT confidence, needs_escalation, latency 
        FROM logs 
        ORDER BY id DESC 
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows


def evaluate_alerts():
    logs = fetch_recent_logs()

    if not logs:
        return None

    confidences = [row[0] for row in logs if row[0] is not None]
    escalations = [row[1] for row in logs]
    latencies = [row[2] for row in logs]

    # P1: repeated escalations
    if escalations.count(True) >= 3:
        return ("P1", "Repeated escalations detected")

    # P2: latency spike
    if any(lat > 2.0 for lat in latencies):
        return ("P2", "Latency spike detected")

    # P2: low confidence trend
    if confidences and sum(confidences)/len(confidences) < 0.6:
        return ("P2", "Low confidence trend")

    return ("P3", "System stable")