def chop(lst):
    if len(lst) > 1:
        lst[:] = lst[1:-1]
    else:
        lst.clear()
my_list = [1, 2, 3, 4, 5]
chop(my_list)
print(my_list)
