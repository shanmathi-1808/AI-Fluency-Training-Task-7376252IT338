"""Day 2, Part B: compare Direct Prompting and Chain-of-Thought."""

from config import client, MODEL, banner, QUESTIONS


DIRECT_PROMPT = (
    "You are a helpful assistant. "
    "Give only the final answer. Do not explain."
)


COT_PROMPT = (
    "You are a helpful assistant. "
    "Solve the problem step by step. "
    "Number each step and show the calculation in that step. "
    "After the steps, write the last line exactly as: "
    "Final Answer: <answer>"
)


def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("CHAIN-OF-THOUGHT COMPARISON")

    for number, question in enumerate(QUESTIONS, start=1):

        print("=" * 72)
        print(f"QUESTION {number}: {question}\n")

        print("--- WITHOUT CoT ---")
        print(
            ask(DIRECT_PROMPT, question),
            "\n"
        )

        print("--- WITH CoT ---")
        print(
            ask(COT_PROMPT, question),
            "\n"
        )