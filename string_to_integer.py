# Write a program to check
# if a string can be converted
# to a valid integer

def is_valid_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
result = is_valid_integer("123")
print(f"Is '123' a valid integer? {result}")

# Using try-except, we attempt to convert the string
# to an integer and catch any ValueError 