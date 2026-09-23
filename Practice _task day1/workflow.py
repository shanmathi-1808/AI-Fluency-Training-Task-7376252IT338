from config import PLANT_RECORDS, QUESTIONS, banner


def get_plant_price(plant_id):
    plant = PLANT_RECORDS.get(plant_id.upper())

    if plant is None:
        return None

    return plant["price"]


def workflow(question):
    question_lower = question.lower()

    if "price of plant p202" in question_lower:
        price = get_plant_price("P202")

        return f"The price of P202 is Rs. {price}."

    if "total price" in question_lower:
        p101 = get_plant_price("P101")
        p505 = get_plant_price("P505")

        total = p101 + p505
        discounted_total = total * 0.90

        return (
            f"The total price of P101 and P505 after "
            f"a 10% discount is Rs. {discounted_total:.2f}."
        )

    if "p505" in question_lower and "p303" in question_lower:
        p505 = get_plant_price("P505")
        p303 = get_plant_price("P303")

        difference = p505 - p303

        if difference > 0:
            return (
                f"Yes. P505 is more expensive than P303 "
                f"by Rs. {difference}."
            )

        elif difference < 0:
            return (
                f"No. P505 is cheaper than P303 "
                f"by Rs. {abs(difference)}."
            )

        else:
            return "P505 and P303 have the same price."

    if "welcome" in question_lower:
        return (
            "Welcome to our plant nursery!\n"
            "We are happy to help you choose the right plants."
        )

    return (
        "Sorry, this rule-based workflow does not "
        "have a rule for that question."
    )


if __name__ == "__main__":
    banner("SYSTEM 2: RULE-BASED WORKFLOW")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)