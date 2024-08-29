def uses_only(word, allowed_letters):
    return set(word).issubset(set(allowed_letters))
print(uses_only("hello", "helo"))
print(uses_only("hello", "hel"))
