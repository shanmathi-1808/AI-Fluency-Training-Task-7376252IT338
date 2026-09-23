"""Day 2: ReAct-style reasoning and tool-use trace."""

from config import client, MODEL, banner


# ------------------------------------------------------------------
# Tool functions
# ------------------------------------------------------------------

def get_electricity_tariff():
    """Return the electricity tariff used in this lab."""

    return 7


def calculator(expression):
    """Safely calculate a basic arithmetic expression."""

    allowed = "0123456789+-*/(). "

    if any(character not in allowed for character in expression):
        return "Invalid expression"

    try:
        return eval(expression, {"__builtins__": {}}, {})
    except Exception as error:
        return f"Calculation error: {error}"


# ------------------------------------------------------------------
# ReAct-style experiment
# ------------------------------------------------------------------

QUESTION = (
    "A house used 240 units of electricity this month. "
    "The electricity tariff is not provided in the question. "
    "Use a tool to obtain the electricity tariff and then "
    "calculate the monthly electricity cost."
)


def run_react():

    print("QUESTION:", QUESTION)
    print("\n--- ReAct trace ---")

    # --------------------------------------------------------------
    # REASON
    # --------------------------------------------------------------

    print("\nThought:")
    print(
        "The electricity tariff is not given, "
        "so I need to obtain it before calculating the cost."
    )

    # --------------------------------------------------------------
    # ACT
    # --------------------------------------------------------------

    print("\nAction:")
    print("get_electricity_tariff()")

    tariff = get_electricity_tariff()

    # --------------------------------------------------------------
    # OBSERVE
    # --------------------------------------------------------------

    print("\nObservation:")
    print(f"Electricity tariff = Rs. {tariff} per unit")

    # --------------------------------------------------------------
    # REASON
    # --------------------------------------------------------------

    print("\nThought:")
    print(
        "Now I can calculate the electricity cost "
        "using 240 units multiplied by the tariff."
    )

    # --------------------------------------------------------------
    # ACT
    # --------------------------------------------------------------

    expression = "240 * " + str(tariff)

    print("\nAction:")
    print(f"calculator('{expression}')")

    cost = calculator(expression)

    # --------------------------------------------------------------
    # OBSERVE
    # --------------------------------------------------------------

    print("\nObservation:")
    print(f"Calculated cost = Rs. {cost}")

    # --------------------------------------------------------------
    # FINAL ANSWER
    # --------------------------------------------------------------

    print("\nFinal Answer:")
    print(
        f"The monthly electricity cost is Rs. {cost} "
        f"at a tariff of Rs. {tariff} per unit."
    )


if __name__ == "__main__":

    banner("REACT TRACE")

    run_react()