# Write a python program
# to find the lowesst common multiple
# of two numbers

import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = lcm(12, 18)
print(f"LCM of 12 and 18 is: {result}")

