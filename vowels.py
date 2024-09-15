# Write a python program
# to count vowels in a
# given string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

result = count_vowels("hello world")
print(f"Number of vowels: {result}")

# We use a generator to count
# the vowels in a string