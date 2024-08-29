list1 = list(map(int, input("Enter sorted list1 elements: ").split()))
list2 = list(map(int, input("Enter sorted list2 elements: ").split()))
merged_list = sorted(list1 + list2)
print("Merged List:", merged_list)
