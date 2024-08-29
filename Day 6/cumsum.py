def cumsum(numbers):
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)
    return result
print(cumsum([1, 2, 3, 4, 5])) 
