def translate_java_line(line):
    line = line.strip()

    if line.startswith("System.out.println"):
        return "Prints text", "Outputs text to the console"
    
    elif line.startswith("for(") or line.startswith("for ("):
        return "For loop", "Loops a fixed number of times or over elements"
    
    elif line.startswith("while(") or line.startswith("while ("):
        return "While loop", "Repeats as long as a condition is true"
    
    elif line.startswith("if(") or line.startswith("if ("):
        return "If statement", "Executes if condition is true"
    
    elif line.startswith("else if"):
        return "Else-if condition", "Alternative condition if previous is false"
    
    elif line.startswith("else"):
        return "Else block", "Executes if all other conditions fail"
    
    elif line.startswith("public class") or line.startswith("class "):
        return "Defines class", "Declares a class (blueprint for objects)"
    
    elif line.startswith("public static void main"):
        return "Main method", "Starting point of the program"
    
    elif "try {" in line:
        return "Try block", "Attempts code that might throw an error"
    
    elif "catch(" in line:
        return "Catch block", "Handles exceptions"
    
    elif line.startswith("import "):
        return "Imports package", "Brings in external classes/libraries"
    
    elif line.startswith("return "):
        return "Returns value", "Sends back result from a method"
    
    elif "new " in line and "(" in line:
        return "Creates object", "Instantiates a new object"
    
    elif "=" in line and "==" not in line:
        return "Assigns value", "Stores data in a variable"
    
    elif "==" in line:
        return "Equality check", "Compares values"
    
    
    else:
        return "Unknown", None
