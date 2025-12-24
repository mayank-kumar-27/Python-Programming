# Compile Function

code = input("Enter Python code: ")
try:
    compiled = compile(code, '<string>', 'eval')
    result = eval(compiled)
    print(f"Result: {result}")
except:
    print("Compilation failed")