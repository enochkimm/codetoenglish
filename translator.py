def translate_line(line):
    line = line.strip()

    if line.startswith("print("):
        content = line[6:-1]
        return f"Prints {content}", "Outputs something to the screen."

    elif line.startswith("for "):
        return "Starts a loop", "Loops over a list, range, or iterable."

    elif line.startswith("if "):
        return "Checks a condition", "Runs code only if the condition is true."

    elif line.startswith("def "):
        return "Defines a function", "Creates a reusable block of code."

    elif line.startswith("return "):
        return "Returns a value", "Sends a value back from a function."

    elif "=" in line and "==" not in line:
        return "Assigns a value", "Stores a value in a variable."

    else:
        return "Performs an action", "No matching rule — might need GPT-4 or advanced logic."
