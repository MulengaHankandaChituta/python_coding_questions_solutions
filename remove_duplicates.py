# Write a python program
# to remove duplicates
# from a list

def remove_duplicates(lst):
    return list(set(lst))

nums = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(nums)
print(f"List after removing duplicates: {result}")

# converting the list to a set
# removes duplicates and converting
# back to a list restores order