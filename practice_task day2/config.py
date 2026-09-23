"""Shared configuration for the Day 2 reasoning experiments."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. "
        "Use ollama, groq or huggingface."
    )

if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}. "
        "Check your .env file."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# Home energy data used for the experiments
ENERGY_DATA = {
    "previous_month_units": 180,
    "current_month_units": 240,
    "solar_generation_units": 60,
    "tariff_per_unit": 7,
}


QUESTIONS = [
    (
        "A house used 180 units of electricity last month and "
        "240 units this month. The electricity tariff is Rs. 7 per unit. "
        "What is the increase in usage and what is the electricity cost "
        "for this month?"
    ),

    (
        "A house used 240 units of electricity this month and generated "
        "60 units through solar panels. The electricity tariff is Rs. 7 "
        "per unit. How many units remain after accounting for solar "
        "generation and what is the effective cost?"
    ),

    (
        "A house used 180 units of electricity last month and "
        "240 units this month. What is the percentage increase "
        "in electricity usage?"
    ),

    (
        "Write a two-line message reminding a homeowner to monitor "
        "electricity usage and make use of solar generation."
    ),
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | model: {MODEL} ===\n"
    )