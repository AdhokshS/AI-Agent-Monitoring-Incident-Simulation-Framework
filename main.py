import json
from app.agent import generate_response
from app.guardrails import apply_guardrails
from app.telemetry import init_db, log_event
from app.monitoring import evaluate_alerts

# Initialize DB
init_db()

print("AI Post-Discharge Assistant (Type 'exit' to quit)\n")

while True:
    user_input = input("Patient: ")

    if user_input.lower() == "exit":
        break

    output, latency = generate_response(user_input)

    try:
        parsed = json.loads(output)

        raw_response = parsed.get("response")
        confidence = parsed.get("confidence")

    except:
        raw_response = "System error. Escalating."
        confidence = 0.0

    # Apply guardrails
    result = apply_guardrails(raw_response, confidence, user_input)

    response = result["response"]
    escalation = result["needs_escalation"]

    print(f"\nAssistant: {response}")
    print(f"Confidence: {confidence}, Escalation: {escalation}, Latency: {latency}s\n")

    # Log
    log_event(user_input, response, confidence, escalation, latency)

    # Alerts
    alert = evaluate_alerts()

    if alert:
        severity, message = alert
        print(f"ALERT [{severity}]: {message}\n")