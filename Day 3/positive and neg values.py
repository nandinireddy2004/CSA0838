positives = 0
negatives = 0
while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
print("Positives:", positives)
print("Negatives:", negatives)
