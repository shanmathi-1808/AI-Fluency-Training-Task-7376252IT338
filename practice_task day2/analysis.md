# Analysis - Reasoning and Acting Comparison

## 1. Scenario

The scenario used in this experiment is based on home electricity usage.

The main data used was:

- Previous month's electricity usage: 180 units
- Current month's electricity usage: 240 units
- Solar generation: 60 units
- Electricity tariff: Rs. 7 per unit

The experiments compare Direct Prompting, Chain-of-Thought (CoT), and ReAct-style tool use.

The reasoning questions involve calculating electricity usage increase, electricity cost, solar generation impact, and percentage increase.

---

## 2. Direct Prompting vs Chain-of-Thought

The same electricity-related questions were given to the model using two different prompting methods.

### Direct Prompting

The direct prompting method instructed the model to provide only the final answer without explanation.

This method produced concise responses and required less output.

For example, for the question involving 180 units last month and 240 units this month:

- Increase in usage = 240 - 180 = 60 units
- Electricity cost = 240 × Rs. 7 = Rs. 1680

### Chain-of-Thought

The Chain-of-Thought prompt instructed the model to solve the problem step by step and show the calculations before giving the final answer.

This made the calculation process more visible and easier to follow.

For numerical questions, the intermediate calculations help verify how the final answer was obtained.

---

## 3. Comparison

| Aspect | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Reasoning depth | Low | Higher | Higher |
| Explanation | Minimal | Step-by-step | Reasoning with actions and observations |
| Tool use | Not required | Not required for these questions | Uses tools when information is required |
| Transparency | Lower | Higher | Higher |
| Speed | Generally faster | More output and processing | Can require additional tool steps |
| Cost | Generally lower | Can use more output tokens | Can increase because of tool interactions |
| Best suited for | Simple questions | Multi-step reasoning | Problems requiring external information or tools |

Direct prompting is useful when a short final answer is sufficient.

Chain-of-Thought is useful when a problem contains multiple reasoning or calculation steps and the solution needs to be easier to inspect.

ReAct is useful when the problem requires information from a tool before completing the answer.

---

## 4. ReAct and Tool Use

The ReAct experiment uses the home electricity scenario.

The question asks the system to calculate the electricity cost when the tariff is not directly provided in the question.

The ReAct-style process is:

1. Identify that the electricity tariff is required.
2. Use the electricity tariff tool.
3. Observe the returned tariff of Rs. 7 per unit.
4. Use the calculator to calculate:

   240 × 7 = Rs. 1680

5. Provide the final answer.

This demonstrates the Reason → Act → Observe pattern.

The tool-based approach is different from direct prompting because the system obtains required information through a tool before completing the calculation.

---

## 5. Self-Consistency Experiment

The first reasoning question was executed five times using a temperature of 0.8.

### Results

| Run | Answer |
|---|---|
| 1 | 60 units, Rs. 1680 |
| 2 | 60 units, Rs. 1680 |
| 3 | Increase in usage: 60 units; Electricity cost: Rs. 1680 |
| 4 | Increase in usage: 60 units; Electricity cost: Rs. 1680 |
| 5 | Increase in usage: 60 units; Electricity cost: Rs. 1680 |

The program reported:

**Majority answer: 60 units, Rs. 1680 (1 of 5 runs)**

However, the five responses are semantically consistent even though their wording is different. The majority calculation in the program compares the complete answer strings, so differently worded answers are treated as different answers.

Therefore, although the program reports 1 out of 5 as the exact-string majority, all five runs produced the same numerical result:

- Increase in usage = 60 units
- Electricity cost = Rs. 1680

This shows that self-consistency can produce consistent reasoning results even when the wording of the final answers changes.

---

## 6. Suitability of Each Method

### Direct Prompting

Direct prompting is suitable for simple questions where only the final answer is required.

For example, asking for the current electricity usage or a short message does not necessarily require a detailed reasoning process.

### Chain-of-Thought

Chain-of-Thought is suitable for calculations and multi-step reasoning.

For example, calculating the increase in electricity usage and the monthly cost requires more than one calculation. Showing the intermediate steps makes the solution easier to inspect.

### ReAct

ReAct is suitable when a problem requires an external tool or additional information.

For example, if the electricity tariff is not given, the system can obtain the tariff using a tool and then use a calculator to calculate the cost.

---

## 7. Reliability and Transparency

Direct prompting gives concise answers but provides limited information about how the answer was obtained.

Chain-of-Thought provides more visible intermediate calculations, which can make numerical reasoning easier to check.

ReAct provides an action-and-observation trace. This makes it possible to see when a tool was used and what information was returned.

Self-consistency provides another way to examine reliability by running the same reasoning problem multiple times at a non-zero temperature.

In this experiment, all five self-consistency runs produced the same numerical result despite differences in wording.

---

## 8. Speed and Cost

Direct prompting generally produces shorter responses and therefore requires less output.

Chain-of-Thought produces additional reasoning steps, which can increase the amount of generated text.

ReAct can require additional model calls and tool calls, so it may take longer than a direct response.

Self-consistency requires multiple runs of the same problem. In this experiment, five runs were performed, so it required more model calls than a single direct or CoT response.

---

## 9. Conclusion

The experiment compared Direct Prompting, Chain-of-Thought, ReAct, and Self-Consistency using a home electricity usage scenario.

Direct Prompting is useful when a concise answer is sufficient.

Chain-of-Thought is useful for problems involving multiple reasoning or calculation steps because the intermediate calculations can be inspected.

ReAct is useful when the problem requires information from an external tool before the final calculation can be completed.

Self-Consistency can be useful for checking whether repeated reasoning produces consistent results. In this experiment, the wording of the five answers varied, but all five produced the same numerical result of 60 units of increased usage and Rs. 1680 electricity cost.

Overall, the experiment demonstrates that different prompting and reasoning approaches can be selected depending on whether the task mainly requires a short answer, detailed reasoning, tool use, or repeated reasoning for consistency.