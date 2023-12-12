import re

with open("day05_input.txt", "rt") as f:
    inputs = f.readlines()

strings = [input.strip() for input in inputs]


def is_nice(string: str) -> bool:
    if re.search(r"(.{2}).*\1", string) and re.search(r"(.).\1", string):
        return True
    return False


nice_strings = [string for string in strings if is_nice(string)]
print(len(nice_strings))
