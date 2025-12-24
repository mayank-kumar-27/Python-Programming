# Eval Exec Functions

# Use with caution - can execute arbitrary code
expression = input("Enter a simple expression: ")
try:
    result = eval(expression)
    print(f"Result: {result}")
except:
    print("Invalid expression")