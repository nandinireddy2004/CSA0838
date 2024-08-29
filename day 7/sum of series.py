total_sum = 0
while True:
    number = int(input("Enter a positive integer (negative number to stop): "))
    if number < 0:
        break
    if number <= 100:
        total_sum += number
print("Total sum:", total_sum)
