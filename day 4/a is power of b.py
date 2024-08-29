def is_power(a, b):
    return a == 1 or (a % b == 0 and is_power(a // b, b))
print(is_power(8, 2)) 
print(is_power(27, 3))  
print(is_power(20, 2)) 
