def print_pascals_triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        value = 1
        for j in range(i + 1):
            print(value, end=' ')
            value = value * (i - j) // (j + 1)
        print()
n = 5
print_pascals_triangle(n)
