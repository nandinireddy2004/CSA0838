def find_missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
arr = [1, 2, 4, 5, 6]
missing_number = find_missing_number(arr)
print(f"The missing number is: {missing_number}")
