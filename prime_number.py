# Write a python program
# to check  if a number
# is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

result = is_prime(36)
print(f"Is 36 prime? {result}")

# We check divisibility up to the
# square root of the number to
# optimize performance