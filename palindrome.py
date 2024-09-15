# Write a function to check if a given string is a palindrome
#(reads the same forwards or backwards)

def is_palindrome(s):
    return s == s[::-1]

result = is_palindrome("radar")
print(f"Is 'radar' a palindrome? {result}")

# We use the slicing method [::-1] to reverse
# the string and to check if it is equal
# to the original string