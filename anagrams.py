# Write a python program
# to check if two strings
# are anagrams

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

result = are_anagrams("listen", "silent")
print(f"Are 'listen' and 'silent' anagrams? {result}")

# We sort both  strings
# and compare if they
# are identical