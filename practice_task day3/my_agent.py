import json

from config import client, MODEL
from my_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a Movie Ticket Assistant.

You help users answer questions about movie tickets.

Use read_webpage when you need information from a movie ticket
HTML file.

Use calculator when arithmetic is required.

Do not guess prices or numbers.
Always use the appropriate tool when information is available
in the provided file.
"""


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

    for step in range(10):

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

            print(
                f"\nTool called: {tool_name}"
            )

            result = TOOL_FUNCTIONS[tool_name](**arguments)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )

    return "Agent stopped after maximum steps."


# -----------------------------
# Main Program
# -----------------------------

questions = [

    "Read movie_tickets.html and tell me the ticket price for Interstellar.",

    "Read movie_tickets.html and calculate the total price for "
    "2 Interstellar tickets and 3 Dune tickets.",

    "Read movie_tickets.html and calculate the total cost for "
    "4 Avengers tickets after the student discount."
]


print("=" * 60)
print("MOVIE TICKET ASSISTANT")
print("=" * 60)


for question in questions:

    print("\nQ:", question)

    answer = run_agent(question)

    print("A:", answer)