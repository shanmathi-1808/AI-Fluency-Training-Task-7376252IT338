import json

from config import client, MODEL
from my_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a Movie Ticket Assistant.

You help users answer questions about movie tickets.

Use read_webpage to read movie ticket information.

Use calculator for arithmetic.

Never guess prices or numbers.
Use the available tools when information is required.
"""


MAX_TOOL_CHARS = 1500
CHAR_BUDGET = 30000
MAX_STEPS = 10
MAX_REPEAT_CALLS = 3


def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    seen_calls = {}
    chars_sent = 0

    for step in range(MAX_STEPS):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message

        messages.append(message)

        if not message.tool_calls:
            return message.content

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            arguments = json.loads(
                tool_call.function.arguments
            )

            signature = (
                tool_name,
                json.dumps(arguments, sort_keys=True)
            )

            seen_calls[signature] = (
                seen_calls.get(signature, 0) + 1
            )

            if seen_calls[signature] > MAX_REPEAT_CALLS:
                return (
                    "Agent stopped because the same tool "
                    "was called repeatedly."
                )

            print(
                f"\nTool called: {tool_name}"
            )

            try:
                result = TOOL_FUNCTIONS[tool_name](**arguments)

            except (TypeError, ValueError, KeyError) as e:
                 result = f"Tool error: {e}"

            if len(result) > MAX_TOOL_CHARS:

                result = (
                    result[:MAX_TOOL_CHARS]
                    + "\n[Observation truncated]"
                )

            chars_sent += len(result)

            if chars_sent > CHAR_BUDGET:
                return (
                    "Agent stopped because the total "
                    "character budget was exceeded."
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )

    return "Agent stopped after maximum steps."


# -----------------------------
# Test Questions
# -----------------------------

questions = [

    "Read movie_tickets.html and tell me the price of "
    "2 Interstellar tickets.",

    "Read movie_tickets.html and calculate the total price "
    "of 2 Interstellar tickets and 3 Dune tickets.",

    "Read movie_tickets.html and calculate the price of "
    "4 Avengers tickets after the student discount.",

    "Read big_movies.html and tell me how many movies "
    "are listed."
]


print("=" * 60)
print("MOVIE TICKET ASSISTANT - GUARDED VERSION")
print("=" * 60)


for question in questions:

    print("\nQ:", question)

    answer = run_agent(question)

    print("A:", answer)