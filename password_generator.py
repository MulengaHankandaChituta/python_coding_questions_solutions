# Write a python program
# to generate a random password
# of a given length

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

password = generate_password(10)
print(f"Generated password: {password}")

# We use random.choice() to select
# random characters from a set
# of letters digits and punctuation