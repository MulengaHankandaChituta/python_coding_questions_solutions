def longest_word(sentencee):
    words = sentencee.split()
    longest = max(words, key=len)
    return longest, len(longest)

word, length = longest_word("The quick brown fox jumped over the lazy dog")
print("The longest word is '{length}")

