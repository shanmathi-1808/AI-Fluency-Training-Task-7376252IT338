import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use groq."
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


# Private plant nursery inventory
PLANT_RECORDS = {
    "P101": {
        "name": "Rose",
        "type": "Flowering Plant",
        "price": 250,
        "quantity": 20
    },
    "P202": {
        "name": "Aloe Vera",
        "type": "Succulent",
        "price": 180,
        "quantity": 15
    },
    "P303": {
        "name": "Money Plant",
        "type": "Indoor Plant",
        "price": 150,
        "quantity": 25
    },
    "P404": {
        "name": "Jasmine",
        "type": "Flowering Plant",
        "price": 220,
        "quantity": 18
    },
    "P505": {
        "name": "Snake Plant",
        "type": "Indoor Plant",
        "price": 300,
        "quantity": 12
    }
}


QUESTIONS = [
    "What is the price of plant P202?",
    "What is the total price of P101 and P505 after a 10% discount?",
    "Is P505 more expensive than P303, and by how much?",
    "Write a two-line welcome message for a new nursery customer.",
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | "
        f"model: {MODEL} ===\n"
    )