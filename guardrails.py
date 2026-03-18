import re

def apply_guardrails(response_text, confidence, user_input=None):

    flagged = False
    escalation = False
    reason = None

    response_lower = response_text.lower()
    user_lower = user_input.lower() if user_input else ""

    # Detect risky medical interpretation
    risky_patterns = [
        r"\byou may have\b",
        r"\byou have\b",
        r"\bit is likely\b",
        r"\bit could be\b",
        r"\bit's not uncommon\b",
        r"\bthis indicates\b",
        r"\bit seems like\b"
    ]

    for pattern in risky_patterns:
        if re.search(pattern, response_lower):
            flagged = True
            escalation = True
            reason = "Medical interpretation detected"
            break

    # Detect medical advice
    advice_patterns = [
        r"\byou should take\b",
        r"\btake medication\b",
        r"\bstart taking\b",
        r"\bincrease dosage\b"
    ]

    for pattern in advice_patterns:
        if re.search(pattern, response_lower):
            flagged = True
            escalation = True
            reason = "Medical advice detected"
            break

    # High-risk symptoms from user input
    high_risk_symptoms = ["fever", "chills", "severe pain", "bleeding", "infection"]

    for symptom in high_risk_symptoms:
        if symptom in user_lower:
            escalation = True
            reason = "High-risk symptom detected"
            break

    # Low confidence
    if confidence is not None and confidence < 0.6:
        escalation = True
        reason = "Low confidence"

    # Override response if needed
    if flagged or escalation:
        safe_response = (
            "I'm here to support your recovery, but your symptoms may require medical attention. "
            "Please contact your healthcare provider for proper guidance."
        )
    else:
        safe_response = response_text

    return {
        "response": safe_response,
        "needs_escalation": escalation,
        "reason": reason
    }