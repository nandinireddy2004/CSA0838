filename = 'name.txt'  # Replace with your file name

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f'The file has {len(lines)} lines.')
except FileNotFoundError:
    print(f'The file {filename} does not exist.')
