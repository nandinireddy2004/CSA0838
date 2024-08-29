result_list = ['over' if int(num) > 100 else int(num) 
               for num in input("Enter integers separated by spaces: ").split()]
print(result_list)
