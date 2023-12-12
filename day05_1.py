import re

with open("day05_input.txt", "rt") as f:
    inputs = f.readlines()

strings = [input.strip() for input in inputs]


def is_nice(string: str) -> bool:
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_string in bad_strings:
        if bad_string in string:
            return False

    if len(re.findall(r"[aeiou]", string)) >= 3 and re.search(r"(.)\1", string):
        return True

    return False


nice_strings = [string for string in strings if is_nice(string)]
print(len(nice_strings))
