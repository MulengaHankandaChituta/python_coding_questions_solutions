# Write a python function
# to print the Fibonacci
# series up to n terms

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

result = fibonacci(7)
print(f"Fibonacci series (7 terms): {result}")

# Using a loop, the Fibonacci sequence is generated
# by updating two variables