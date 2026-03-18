# 🏥 AI Agent Monitoring & Incident Simulation Framework

## 🚀 Overview
This project simulates a **safety-first AI agent system for healthcare workflows**, focused on post-discharge patient follow-up.

The goal is not just to generate responses, but to demonstrate how AI agents should be **monitored, controlled, and escalated in production environments**, especially in safety-critical domains like healthcare.

---

## 🧠 Core Idea

> AI in healthcare should not just be intelligent — it must be **observable, safe, and operationally reliable**.

This system reflects how AI agents should behave:
- ✅ Assist, not diagnose  
- ✅ Escalate when uncertain  
- ✅ Be monitored continuously  
- ✅ Operate within strict safety boundaries  

---

## 🏗️ System Architecture

The system is designed with **four core layers**:

### 1️⃣ Agent Layer
- Handles patient interaction using LLM (Groq)
- Generates structured output (response + confidence)

### 2️⃣ Guardrail Layer
- Enforces safety constraints
- Prevents diagnosis and medical advice
- Detects high-risk symptoms (e.g., fever, chills)
- Forces escalation when risk is detected

### 3️⃣ Telemetry Layer
- Logs operational signals:
  - Response latency  
  - Confidence score  
  - Escalation flags  
- Stores structured logs in SQLite

### 4️⃣ Monitoring Layer
- Evaluates recent system behavior
- Simulates production alerting logic:

| Severity | Trigger Condition |
|--------|----------------|
| 🔴 P1 (Critical) | Repeated escalations |
| 🟡 P2 (Warning) | Latency spike / low confidence |
| 🟢 P3 (Normal) | Stable system behavior |

---

## ⚙️ Example Flow

1. Patient reports symptoms  
2. Agent generates structured response  
3. Guardrails validate safety  
4. System logs telemetry  
5. Monitoring layer evaluates patterns  
6. Alerts triggered based on system behavior  

---

## 🔒 Safety Design Principles

- ❌ No diagnosis  
- ❌ No medical advice  
- ✅ Escalate when uncertain  
- ✅ Prioritize patient safety over response quality  

---

## 🧪 Sample Test Cases

### 🔴 High-Risk Input
