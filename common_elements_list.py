# Write a python function to find
# the common elements in two lists

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = common_elements(list1, list2)
print(f"Common elements: {result}")

# The & operator finds the intersection of 
# two sets and we convert the result back t a list