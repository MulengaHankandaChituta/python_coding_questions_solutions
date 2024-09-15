# Write a python program
# that returns the factorial
# of a number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(40)
print(f"Factorial of 40 is: {result}")

# The program uses recursion,  where the
# function calls itself until it reaches
# the base case of 0