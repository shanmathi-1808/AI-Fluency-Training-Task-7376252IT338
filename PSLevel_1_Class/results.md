# Day 8 — Agentic AI: Foundations and Open-Source Practice

## Part A — Placement Policy Ingestion and Search

### 1. Placement Policy Document

Created `data/placement_policy.md` containing the Greenfield College of Engineering sample placement policy.

The policy includes:
- Minimum CGPA of 6.5 with no standing arrears.
- Registration on the placement portal before 31 July of the final year.
- Minimum 90% attendance in pre-placement training.
- Students receiving an offer of 6 LPA or above cannot attend further drives.
- Students placed below 6 LPA may attend one more drive for a dream offer of at least 1.5 times their current package.

### 2. Search Results from `2_search.py`

**Command executed:**

```powershell
python 2_search.py
```

#### Test 1: Late Fee

**Question:** How much is the late fee for paying fees after the due date?

| Score | Source | Retrieved information |
|---:|---|---|
| 0.186 | `fee_policy.md` | A late fee of Rs. 100 per day is charged after the due date. |
| 0.297 | `fee_policy.md` | Tuition fee payment information |
| 0.337 | `exam_regulations.md` | Revaluation information |

**Result:** Pass. The top result contains the late fee information from `fee_policy.md`.

#### Test 2: Hostel Return Time

**Question:** What time should hostel students return?

| Score | Source | Retrieved information |
|---:|---|---|
| 0.137 | `hostel_rules.md` | Hostel residents must return by 9.00 PM. |
| 0.249 | `hostel_rules.md` | Hostel rules document |
| 0.317 | `hostel_rules.md` | Leave form information |

**Result:** Pass. The top result contains the hostel return-time rule.

#### Test 3: Exam Attendance

**Question:** Can I write the exam with 70% attendance?

| Score | Source | Retrieved information |
|---:|---|---|
| 0.235 | `exam_regulations.md` | Information about students below 65% attendance |
| 0.246 | `exam_regulations.md` | A minimum of 75% attendance is required in each course |
| 0.278 | `exam_regulations.md` | Examination regulations document |

**Result:** Pass. The search retrieves relevant examination attendance information.

#### Test 4: Placement Eligibility

**Question:** What CGPA do I need to be eligible for placements?

| Score | Source | Retrieved information |
|---:|---|---|
| 0.185 | `placement_policy.md` | Placement policy document |
| 0.252 | `fee_policy.md` | Scholarship information |
| 0.284 | `placement_policy.md` | Pre-placement training attendance requirement |

**Result:** Pass. The top result is from `placement_policy.md`, confirming that the new placement policy is available in the search system.

#### Test 5: Library Document Filter

The output filtered results to `library.md` and retrieved:
- Library fine information: Rs. 2 per day per book for late returns.
- The Library Rules document.
- Information about borrowing books.

**Result:** Pass. The filter returned library-related passages.

### Part A Conclusion

The search tests retrieved relevant passages from the expected source documents for late fees, hostel rules, exam attendance, and placement eligibility. The placement question returned `placement_policy.md` as its top result.

---

## Part B — Exam Eligibility Tool

Implemented the `check_exam_eligibility(attendance_percent)` tool.

### Eligibility Rules

| Attendance | Expected result |
|---|---|
| 75% or above | Eligible |
| 65% to below 75% | Condonation: Rs. 500 per course |
| Below 65% | Not eligible |
| Below 0% or above 100% | Error message |

### Direct Tool Tests

| Attendance | Expected output |
|---:|---|
| 82% | Eligible |
| 70% | Condonation: Rs. 500 per course |
| 50% | Not eligible |
| 120% | Error: attendance must be between 0 and 100 |

### Agent Test

**Question:** My attendance is 70%. Can I write the exam?

The tool returned:

`CONDONATION: Rs. 500 per course.`

In one run, the agent gave the correct condonation explanation. In a later run, it answered, “I’m sorry, but I don’t have that information.”

**Status:** The tool itself returned the expected result, but the agent's final response was inconsistent. This should be retested after adjusting the system prompt.

---

## Part C — Similarity Threshold and No-Match Handling

Updated `search_handbook()` to use:

```python
store.similarity_search_with_score(query, k=3)
```

The function prints search scores, filters results using `MAX_DISTANCE`, and returns a no-match message when no results pass the threshold:

`NO_MATCH: this is not covered in the college handbook.`

### Configuration

- **MAX_DISTANCE:** 0.5, if this is the final value currently saved in `task_agent.py`.
- **Placement search scores:** 0.1815, 0.2306, 0.3210 from the agent run.
- **Exam attendance search scores:** 0.1814, 0.2450, 0.2762.
- **AI202 fee search scores:** 0.3278, 0.3444, 0.3496.
- **Late fee maximum search scores:** 0.1621, 0.3256, 0.3536.

The above scores are from the terminal output. The scores printed by `2_search.py` are recorded separately in Part A.

### No-Match Test

**Question:** What is the capital of France?

**Observed answer:** “I don’t know.”

**Result:** Pass. The agent did not answer from general knowledge when the handbook did not cover the question.

**Note:** The France search scores were not included in the terminal output provided for this report. Add those scores if they are printed in a later run.

---

## Part D — Agent Test Results

The agent was tested with five questions in the same conversation thread, `task-run`.

| # | Question | Tools called, in order | Answer / observed behavior | Correct? |
|---|---|---|---|---|
| 1 | What CGPA do I need to be eligible for placements? | `search_handbook` | CGPA of 6.5 or above and no standing arrears. Source: `placement_policy.md`. | Y |
| 2 | My attendance is 70%. Can I write the exam? | `check_exam_eligibility`, `search_handbook` in the first run; `check_exam_eligibility` in the second run | One run returned the correct condonation explanation. Another returned “I don’t have that information.” | N — inconsistent |
| 3 | What is the total of the CS101 fee, the AI202 fee and the maximum late fee? | `search_handbook`, `get_course_fee`, `get_course_fee`, `calculator` | Rs. 32,000 = Rs. 12,000 + Rs. 18,000 + Rs. 2,000. | Y |
| 4 | And if I pay only 5 days late instead? | `calculator` | Rs. 30,500 = Rs. 12,000 + Rs. 18,000 + Rs. 500. | Y |
| 5 | What is the capital of France? | No tool call shown in the final run | “I don’t know.” | Y |

### Fee Calculation Details

**Question 3:**

- CS101 fee: Rs. 12,000
- AI202 fee: Rs. 18,000
- Maximum late fee: Rs. 2,000
- Calculator expression: `12000 + 18000 + 2000`
- Total: **Rs. 32,000**

**Question 4:**

- CS101 fee: Rs. 12,000
- AI202 fee: Rs. 18,000
- Late fee for 5 days: 5 × Rs. 100 = Rs. 500
- Calculator expression: `12000 + 18000 + 500`
- Total: **Rs. 30,500**

### Agent Test Conclusion

The agent correctly answered the placement question, calculated the two fee totals, and declined to answer the unrelated France question. The exam eligibility tool returned the correct condonation result, but the agent did not consistently use that result in its final response.

---


