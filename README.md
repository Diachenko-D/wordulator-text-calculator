# wordulator-text-calculator - natural language Text Calculator

A CLI Python application that parses natural language mathematical expressions written in text, converts word numerals into numbers, and computes simple arithmetic operations

---

## Syntax Overview
* **Supported Operations:**
  * `plus` → Addition (`+`)
  * `minus` → Subtraction (`-`)
  * `multiplied by` → Multiplication (`*`)
  * `divided by` → Division (`/`) — outputs up to 8 decimal places
* **Numeral Range:** `-999,999` to `999,999`
* **Negative Support:** Handles double negatives (e.g., `eighty minus minus two = 82`)
* **Error Handling:** Gracefully handles spelling errors, out-of-range commands, and division by zero

---

## How to Run

### Prerequisites
* Python 3.x installed

### To Run
1. Clone or download this repository
2. Run the script

### Repository Structure
main.py: Lexical parser, tokenizer, evaluation logic, and CLI loop
specifications.md: Project constraints and specifications
example_4.txt: Console execution examples
