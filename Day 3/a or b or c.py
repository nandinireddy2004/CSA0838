choice = input("Enter 'A', 'B', or 'C': ")
words = {'A': 'Apple', 'B': 'Banana', 'C': 'Coconut'}
print(words.get(choice, "Invalid input."))
