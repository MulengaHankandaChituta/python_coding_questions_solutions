# Write a python program
# to calculate the sum
# of digits of a given number

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

result = sum_of_digits(12345)
print(f"Sum of digits of 12345: {result}")

# Convert the number to a string
# loop over each digit
# and sum the integer values