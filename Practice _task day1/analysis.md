# Analysis – Plant Nursery Inventory

## 1. Scenario

The scenario used for this practice task is a Plant Nursery Inventory system.

The private inventory contains five plant records:

- P101 – Rose – Flowering Plant – Rs. 250 – Quantity 20
- P202 – Aloe Vera – Succulent – Rs. 180 – Quantity 15
- P303 – Money Plant – Indoor Plant – Rs. 150 – Quantity 25
- P404 – Jasmine – Flowering Plant – Rs. 220 – Quantity 18
- P505 – Snake Plant – Indoor Plant – Rs. 300 – Quantity 12

The same set of questions was tested using three approaches:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

---

## 2. Plain Chatbot

The plain chatbot uses the language model to generate responses.

It can answer general questions and create natural-language responses, but it does not have direct access to the private nursery inventory.

For example, when asked for the price of P202, the chatbot does not automatically retrieve the private record.

### Strengths

- Flexible for natural-language questions.
- Good for generating welcome messages and general explanations.
- Simple to implement.

### Limitations

- Cannot directly access private inventory data.
- May not know the correct plant prices unless the information is provided in the prompt.
- Not suitable for reliable inventory lookups by itself.

---

## 3. Rule-Based Workflow

The rule-based workflow uses predefined Python rules and directly accesses the nursery inventory data.

For example, specific rules handle:

- The price of P202.
- The total price of P101 and P505 after a discount.
- The price difference between P505 and P303.
- A welcome message.

### Strengths

- Gives predictable results for predefined questions.
- Directly accesses the private inventory records.
- Arithmetic and decisions can be controlled by Python code.
- Does not depend on the language model for the predefined rules.

### Limitations

- Requires a new rule when a new type of question is introduced.
- Less flexible with unexpected wording or new tasks.
- More difficult to maintain as the number of rules increases.

---

## 4. AI Agent

The AI agent combines an LLM, tools, and a loop.

The agent can use the `get_plant_record` tool to access private nursery inventory information and the `calculator` tool for arithmetic.

For example, for the discount question, the agent can:

1. Retrieve the record for P101.
2. Retrieve the record for P505.
3. Use the calculator for the discount calculation.
4. Generate a final natural-language answer.

This demonstrates multi-step task handling.

### Strengths

- Can decide which tool is needed.
- Can access private inventory through a controlled tool.
- Can handle multiple steps in a single task.
- More flexible than a fixed rule-based workflow.
- Can combine data retrieval, calculation, and natural-language responses.

### Limitations

- Depends on correct tool selection and tool calls.
- More complex than a simple chatbot or fixed workflow.
- Errors can occur if the model generates an invalid tool call.
- Requires testing and monitoring for reliable results.

---

## 5. Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for natural language | Low for unexpected questions | High |
| Decision-making | Mainly generates responses | Predefined by rules | Can select tools and steps |
| Tool usage | No tools | Uses programmed functions | Uses LLM-selected tools |
| Private-data access | No direct access | Direct access through code | Controlled access through tools |
| Multi-step task handling | Limited | Predefined steps | Can perform multiple tool calls |
| Automation | Basic | High for predefined tasks | High for dynamic tasks |
| Reliability | Depends on model response | Predictable for defined rules | Depends on model and tools |

---

## 6. Suitability for the Nursery Inventory Scenario

### Plain Chatbot

The plain chatbot is suitable for general customer communication, such as welcome messages and simple explanations.

It is less suitable for answering private inventory questions because it does not directly access the inventory records.

### Rule-Based Workflow

The rule-based workflow is suitable when the nursery has a small number of fixed operations.

It provides predictable results, but adding new questions requires additional rules.

### AI Agent

The AI agent is suitable when customers or staff may ask different types of inventory questions that require data retrieval and calculations.

It can combine private-data access, calculations, and natural-language responses in a multi-step process.

---

## 7. Challenge Question

The challenge question was:

**Which plants have a price above Rs. 220?**

The inventory contains:

- P101 – Rose – Rs. 250
- P505 – Snake Plant – Rs. 300

Therefore, the matching plants are **P101 (Rose)** and **P505 (Snake Plant)**.

The rule-based implementation checks every inventory record against the condition `price > 220`.

The AI agent can also use the available inventory tool and reason over the returned records.

---

## 8. Reliability and Limitations

The rule-based workflow provides predictable results when the question matches one of its predefined rules.

The AI agent provides more flexibility, but its reliability depends on correct tool selection and valid tool calls.

During testing, the AI agent successfully retrieved plant records, but the Groq model produced an invalid calculator tool name during one calculation. This shows that an AI agent requires testing and error handling even when the underlying tools are correct.

---

## 9. Conclusion

The three approaches solve the same scenario in different ways.

A plain chatbot is useful for general language-based interaction.

A rule-based workflow is useful for predictable and predefined inventory operations.

An AI agent combines language understanding with tools and a loop, allowing it to perform more flexible multi-step tasks involving private inventory data.

The choice of approach depends on the task requirements, especially the need for flexibility, private-data access, predictable rules, and multi-step automation.