import ast
import operator
import os
import re
import requests


# -----------------------------
# Calculator Tool
# -----------------------------

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def evaluate(node):

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        operation = OPS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        value = evaluate(node.operand)

        operation = OPS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        return operation(value)

    raise ValueError("Invalid expression")


def calculator(expression: str):

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)
        return str(result)

    except Exception as e:
        return f"Calculator error: {e}"


# -----------------------------
# HTML / File Reader Tool
# -----------------------------

def read_webpage(url: str, max_chars: int = 2000):

    try:

        if url.startswith("http://") or url.startswith("https://"):

            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            response.raise_for_status()

            html = response.text

        elif os.path.exists(url):

            with open(url, "r", encoding="utf-8") as file:
                html = file.read()

        else:
            return "File not found."

        html = re.sub(
            r"<script.*?>.*?</script>",
            " ",
            html,
            flags=re.DOTALL | re.IGNORECASE
        )

        html = re.sub(
            r"<style.*?>.*?</style>",
            " ",
            html,
            flags=re.DOTALL | re.IGNORECASE
        )

        html = re.sub(r"<[^>]+>", " ", html)

        html = re.sub(r"\s+", " ", html).strip()

        return html[:max_chars]

    except Exception as e:
        return f"Error reading webpage: {e}"


# -----------------------------
# Tool Functions
# -----------------------------

TOOL_FUNCTIONS = {
    "calculator": calculator,
    "read_webpage": read_webpage
}


# -----------------------------
# OpenAI Tool Schemas
# -----------------------------

TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform safe arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "read_webpage",
            "description": "Read text from a webpage or local HTML file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL or local HTML file path."
                    }
                },
                "required": ["url"]
            }
        }
    }
]