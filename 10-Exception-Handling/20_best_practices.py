# Best Practices

# Use specific exceptions
# Don't catch Exception broadly
# Use finally for cleanup
# Keep try blocks small

try:
    num = int(input("Enter number: "))
    if num < 0:
        raise ValueError("Positive numbers only")
    print(f"Number: {num}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Execution complete")