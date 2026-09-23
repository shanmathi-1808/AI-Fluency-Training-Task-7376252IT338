import ast
import operator

from config import PLANT_RECORDS


def get_plant_record(plant_id: str) -> str:
    plant_id = plant_id.strip().upper()

    record = PLANT_RECORDS.get(plant_id)

    if record is None:
        return f"Unknown plant ID: {plant_id}"

    return (
        f"Plant ID: {plant_id}, "
        f"Name: {record['name']}, "
        f"Type: {record['type']}, "
        f"Price: Rs. {record['price']}, "
        f"Quantity: {record['quantity']}"
    )


_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def _evaluate(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp):
        if type(node.op) in _OPS:
            return _OPS[type(node.op)](
                _evaluate(node.left),
                _evaluate(node.right)
            )

    if isinstance(node, ast.UnaryOp):
        if type(node.op) in _OPS:
            return _OPS[type(node.op)](
                _evaluate(node.operand)
            )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    try:
        result = _evaluate(
            ast.parse(expression, mode="eval").body
        )

        return str(result)

    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_plant_record": get_plant_record,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_plant_record",
            "description": (
                "Get private nursery inventory information "
                "for a plant ID such as P101, P202, P303, "
                "P404, or P505."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "plant_id": {
                        "type": "string"
                    }
                },
                "required": ["plant_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Evaluate an arithmetic expression using "
                "+, -, *, / and brackets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"],
            },
        },
    },
]