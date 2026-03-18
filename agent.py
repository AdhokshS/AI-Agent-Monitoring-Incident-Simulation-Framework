import os
import time
from groq import Groq

client = Groq(api_key="YOUR_API_KEY_HERE")

def generate_response(user_input):
    start_time = time.time()

    prompt = f"""
    You are a healthcare follow-up assistant.

    Rules:
    - You are NOT a doctor.
    - Do NOT diagnose.
    - Do NOT provide medical advice.
    - Only assist with post-discharge follow-up.
    - If unsure or risk detected, recommend contacting a healthcare professional.

    Patient Input: {user_input}

    Respond in JSON format:
    {{
        "response": "...",
        "confidence": 0.0 to 1.0,
        "needs_escalation": true/false
    }}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    output = completion.choices[0].message.content
    latency = round(time.time() - start_time, 3)

    return output, latency