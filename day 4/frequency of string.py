def most_frequent(s):
    freq = {char: s.count(char) for char in s}
    print(''.join(sorted(freq, key=freq.get, reverse=True)))
most_frequent("banana")
