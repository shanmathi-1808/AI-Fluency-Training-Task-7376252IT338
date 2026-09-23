"""Day 2, Part C: self-consistency with multiple CoT runs."""

from collections import Counter

from config import (
    client,
    MODEL,
    banner,
    QUESTIONS
)

from cot_compare import COT_PROMPT


RUNS = 5
TEMPERATURE = 0.8


def final_answer(text):
    """Extract the final answer from a CoT response."""

    for line in reversed(text.splitlines()):

        if "final answer" in line.lower():

            return line.split(
                ":",
                1
            )[-1].strip()

    if text.strip():
        return text.splitlines()[-1].strip()

    return "(empty)"


def run_many(
    question,
    runs=RUNS,
    temperature=TEMPERATURE
):

    answers = []

    for attempt in range(1, runs + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=temperature,
        )

        answer = final_answer(
            response.choices[0].message.content
        )

        print(
            f"   run {attempt}: {answer}"
        )

        answers.append(answer)

    return answers


if __name__ == "__main__":

    banner("SELF-CONSISTENCY")

    # Use the first reasoning question
    question = QUESTIONS[0]

    print(
        "QUESTION:",
        question,
        "\n"
    )

    answers = run_many(question)

    counts = Counter(answers)

    majority_answer, count = counts.most_common(1)[0]

    print(
        f"\nMajority answer "
        f"({count} of {len(answers)} runs): "
        f"{majority_answer}"
    )