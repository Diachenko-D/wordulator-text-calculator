unique_units = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
}
tens = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
hundreds = {
    "one hundred": 100,
    "two hundred": 200,
    "three hundred": 300,
    "four hundred": 400,
    "five hundred": 500,
    "six hundred": 600,
    "seven hundred": 700,
    "eight hundred": 800,
    "nine hundred": 900,
}

def parse_parts(words): # Reads a list of words and converts them into a number (works for numbers under 1000)
    if not words: # No words, no number
        return 0
    num = 0
    i = 0
    
    # Check if first word(s) represent hundreds
    if len(words) >= 2 and f"{words[0]} {words[1]}" in hundreds:
        num += hundreds[f"{words[0]} {words[1]}"]
        i += 2
    elif i < len(words) and words[i] in hundreds:
        num += hundreds[words[i]]
        i += 1

    if i < len(words):
        rest = words[i:] # Keep only tens and units
        rest_str = " ".join(rest)
        
        # Check if remaining string is a unit, teenager, ten, or ten+unit
        if rest_str in unique_units:
            num += unique_units[rest_str]
        elif len(rest) == 1 and rest[0] in tens:
            num += tens[rest[0]]
        elif len(rest) == 2 and rest[0] in tens and rest[1] in unique_units and unique_units[rest[1]] < 10:
            num += tens[rest[0]] + unique_units[rest[1]]
        else:
            raise ValueError()
    return num

def word_to_num(s: str) -> int: # Converts string text into a final number
    if not s.strip(): # Empty string raises an error
        raise ValueError()
    words = s.lower().split() # Convert string to lowercase for convenience
    negative = False
    if words[0] == "minus": # Check if "minus" is before the word (negative number)
        negative = True
        words = words[1:]
        if not words:
            raise ValueError()

    total = 0
    thousand_check = -1 # Look for the word "thousand" to see if thousands order exists
    for j, w in enumerate(words):
        if "thousand" in w:
            thousand_check = j
            break

    if thousand_check != -1: # If "thousand" is found, split word into two parts
        thousands_part = words[:thousand_check] # Part with thousands
        if not thousands_part: # If no words before "thousand", value is 1
            th_val = 1
        else:
            th_val = parse_parts(thousands_part) # Read string and make it a number
        remainder_part = words[thousand_check + 1:] # Part with hundreds, tens, and units
        rem_val = parse_parts(remainder_part)
        total = th_val * 1000 + rem_val # Sum thousands part and hundreds/tens/units part
    else:
        total = parse_parts(words) # If no "thousand", convert string directly to number
    return -total if negative else total # If minus was present at start, return negative number

def tokenize(text: str): # Separates numbers from operations
    words = text.lower().split()
    if not words:
        raise ValueError()

    tokens = []
    i = 0

    num_words = [] # List of number words
    if words[0] == "minus": # If minus is first word, it's a sign before number; add to list
        num_words.append("minus")
        i = 1
    while i < len(words):
        w = words[i]
        if w in {"plus", "minus", "multiplied", "divided"}: # Stop when reaching an operation
            break
        num_words.append(w)
        i += 1

    if not num_words or num_words == ["minus"]:
        raise ValueError()
    tokens.append(word_to_num(" ".join(num_words))) # Convert string to numbers and add to list

    while i < len(words): # Work with commands, identify command and convert to corresponding operator
        if words[i] == "plus":
            op = "+"
            i += 1
        elif words[i] == "minus":
            op = "-"
            i += 1
        elif words[i] == "multiplied" and i + 1 < len(words) and words[i + 1] == "by":
            op = "*"
            i += 2
        elif words[i] == "divided" and i + 1 < len(words) and words[i + 1] == "by":
            op = "/"
            i += 2
        else:
            raise ValueError()
        tokens.append(op) # Add operator to element list

        num_words = [] # Next word, work on same principle as first
        if i < len(words) and words[i] == "minus":
            num_words.append("minus")
            i += 1
        while i < len(words):
            w = words[i]
            if w in {"plus", "minus", "multiplied", "divided"}:
                break
            num_words.append(w)
            i += 1

        if not num_words: # Empty list = error
            raise ValueError()
        tokens.append(word_to_num(" ".join(num_words)))

    return tokens # Return full list


def count(tokens): # Calculates the result of input
    if not tokens or not isinstance(tokens[0], (int, float)):
        raise ValueError()
    result = tokens[0] # Start with first word
    i = 1
    while i < len(tokens):
        op = tokens[i] # Add operation
        b = tokens[i + 1] # Add number
        if op == "+":
            result += b
        elif op == "-":
            result -= b
        elif op == "*":
            result *= b
        elif op == "/":
            if b == 0:
                raise ValueError("You will divide by zero at university, you can't here") # Divide by zero error
            result /= b
        else:
            raise ValueError()
        i += 2
    return result # Return result


def output(x): # Formats output
    if isinstance(x, int): # If integer, print as is
        return str(x)
    s = f"{x:.8f}".rstrip('0').rstrip('.') # Round to 8 decimal places per spec
    return s

def main():
    print("Hello, this is Text Calculator. I have a limited set of operations and small input rules)\n")
    print("Supported operations:")
    print(' - "plus" → addition (+)')
    print(' - "minus" → subtraction (-)')
    print(' - "multiplied by" → multiplication (*)')
    print(' - "divided by" → division (/)')
    print("\nNumber range: from -999999 to 999999.")
    print('Enter whatever you want within range, write capitalized or lowercase, and watch your spelling (please)\n')
    print('Here is an example: eighty minus minus two = 82\n')
    print('To exit, enter: exit\n')

    while True:
        inp = input("> ").strip()
        if inp.lower() == "exit":
            print("Bye!")
            break
        if not inp:
            print("\nInvalid input")
            continue
        try:
            tokens = tokenize(inp)
            result = count(tokens)
            print(inp, f" = {output(result)}")
        except ValueError as e:
            if "You will divide by zero at university" in str(e):
                print("\nYou will divide by zero at university, you can't here")
            else:
                print("\nInvalid input")
        except Exception:
            print("\nInvalid input")

main()
