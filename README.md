AI Agent Monitoring & Incident Simulation Framework
Overview

This project simulates a safety-first AI agent system for healthcare workflows, focused on post-discharge patient follow-up.

The system is designed to demonstrate how AI agents should be monitored, controlled, and escalated in production environments, particularly in safety-critical domains like healthcare.

Architecture

The system is built with four core layers:

1. Agent Layer

Handles patient interaction using LLM (Groq)

Produces structured output (response, confidence)

2. Guardrail Layer

Enforces safety constraints

Prevents diagnosis and medical advice

Detects high-risk symptoms and forces escalation

3. Telemetry Layer

Logs system behavior (latency, confidence, escalation)

Stores structured logs in SQLite

4. Monitoring Layer

Evaluates recent system activity

Generates severity-based alerts:

P1: Critical (repeated escalations)

P2: Warning (latency / confidence issues)

P3: Normal operation

Key Features

Safety-first AI behavior (non-diagnostic)

Deterministic guardrails over LLM outputs

Confidence-aware escalation logic

Structured telemetry logging

Alert simulation (P1 / P2 / P3)

Incident-style system behavior

Example Flow

User reports symptoms

Agent generates structured response

Guardrails validate safety

System logs telemetry

Monitoring layer evaluates patterns

Alerts triggered based on system behavior

Why This Matters

In healthcare AI systems:

Accuracy alone is not sufficient

Safety, monitoring, and escalation are critical

This project demonstrates how AI systems should be:

Observed

Controlled

Integrated into operational workflows

Tech Stack

Python

Groq API (LLM)

SQLite

Streamlit (planned)

Future Enhancements

Real-time monitoring dashboard

Note: API keys are managed via environment variables and are not stored in the repository.

Alert visualization

SLA tracking

Incident playbooks
