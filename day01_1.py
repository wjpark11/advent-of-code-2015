with open("day01_input.txt", "rt") as f:
    inputs = f.readlines()

instruction = [input.strip() for input in inputs][0]

floor = 0
for symbol in instruction:
    if symbol == "(":
        floor += 1
    elif symbol == ")":
        floor -= 1

print(floor)
