# write a python program
# to  find the missing
# number from an array
# containing n distinct
# integers in the range
# 1 to n + 1

def find_missing(arr):
    n = len(arr) +  1
    total_sum = n * (n + 1) // 2
    return total_sum -  sum(arr)

nums = [1, 2, 4, 5]
missing = find_missing(nums)
print(f"Missing number: {missing}")

# The sum of the first n numbers is subtracted from
# the sum of the array to find the missing number