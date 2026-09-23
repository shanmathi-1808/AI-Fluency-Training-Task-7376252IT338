from config import PLANT_RECORDS, banner
from agent import agent


CHALLENGE = (
    "Which plants have a price above Rs. 220?"
)


def rule_based_challenge():

    matching_plants = []

    for plant_id, record in PLANT_RECORDS.items():

        if record["price"] > 220:
            matching_plants.append(
                f"{plant_id} ({record['name']})"
            )

    return ", ".join(matching_plants)


if __name__ == "__main__":

    banner("CHALLENGE")

    print("Question:", CHALLENGE)

    print("\nRule-based result:")
    print(rule_based_challenge())

    print("\nAgent result:")
    print(agent(CHALLENGE))