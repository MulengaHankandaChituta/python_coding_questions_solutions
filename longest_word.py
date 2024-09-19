# Write a python program to find the longest
# word in a sentence and it's length

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest, len(longest)

words, length = longest_word("I'm fulfilling my journey to being a backend developer")
print(f"The longest word is '{words}' with length {length}")

# split the sentence into words
# and use max() with key=len
# to find the longest word
