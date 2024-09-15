# Swap two numbers without using a third variable
# Write a python function to swap two numbers without using a temporary variable

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

a = 5
b = 10
a, b = swap(a, b)
print(f"After swapping: a = {a}, b = {b}")

# Used simple addition and subtraction to swap numbers
