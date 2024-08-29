def are_triangular(a, b, c):
    return a < b + c and b < a + c and c < a + b
print(are_triangular(3, 4, 5)) 
print(are_triangular(1, 2, 3)) 
