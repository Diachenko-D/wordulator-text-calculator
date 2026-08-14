Specification for Calculator

The calculator is implemented in the terminal. Since the technical requirements are broad, we first display all available commands and input rules to the user.

A string containing the text of a mathematical expression written in natural language is passed to the input. It is necessary to parse what mathematical expression it is and evaluate it.

It is guaranteed that input is provided in natural text, following standard language grammar rules. In case of an error, the program outputs: Invalid input

Number range for input: from -999 999 to 999 999.
Input in the format (where x is some number) is permitted: minus x minus minus x, which is equivalent to -x - (-x) = -x + x.
If a number is entered simply as a word, we output the number in digits.

List of available commands:
- addition (command: ... plus ...) - "+"
- subtraction (command: ... minus ...) - "-"
- multiplication (command: ... multiplied by ...) - "*"
- division (command: divided ... by ...) - "/" Output rounded up to 8 decimal places

Note: Parsing individual word stems directly can be tricky due to complex natural language numeral inflections. Explicitly mapping each place value turns out to be much simpler and more robust!
