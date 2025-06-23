def translate_line(line):
    line = line.strip()

    if line.startswith("print("):
        return "Prints text", "Outputs to console"
    
    elif line.startswith("for "):
        return "Starts loop", "Repeats over items"
    
    elif line.startswith("while "):
        return "While loop", "Repeats while condition true"
    
    elif line.startswith("if "):
        return "Checks condition", "Runs if true"
    
    elif line.startswith("elif "):
        return "Else-if check", "Alternate condition"
    
    elif line.startswith("else"):
        return "Else block", "Runs if previous failed"
    
    elif line.startswith("def "):
        return "Defines function", "Creates reusable code"
    
    elif line.startswith("return "):
        return "Returns value", "Exits with result"
    
    elif line.startswith("import "):
        return "Imports module", "Loads external code"
    
    elif line.startswith("from "):
        return "Imports part", "Loads specific function/module"
    
    elif line.startswith("class "):
        return "Defines class", "Creates object blueprint"
    
    elif "try:" in line:
        return "Try block", "Attempts risky code"
    
    elif "except" in line:
        return "Except block", "Handles error"
    
    elif "with open(" in line:
        return "File open", "Handles file safely"
    
    elif "[" in line and "]" in line and "for" in line:
        return "List comp", "Compact loop for list"
    
    elif "=" in line and "==" not in line:
        return "Assigns value", "Stores data"
    
    elif "==" in line:
        return "Equality check", "Compares values"
    
    else:
        return "Unknown", None 
