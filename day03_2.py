with open("day03_input.txt", "rt") as f:
    inputs = f.readlines()

instructions = inputs[0].strip()

gifted_houses = {
    (0, 0),
}

current_house = (0, 0)
for inst in instructions[::2]:
    if inst == "^":
        current_house = (current_house[0], current_house[1] + 1)
    elif inst == "v":
        current_house = (current_house[0], current_house[1] - 1)
    elif inst == ">":
        current_house = (current_house[0] + 1, current_house[1])
    elif inst == "<":
        current_house = (current_house[0] - 1, current_house[1])
    gifted_houses.add(current_house)

current_house = (0, 0)
for inst in instructions[1::2]:
    if inst == "^":
        current_house = (current_house[0], current_house[1] + 1)
    elif inst == "v":
        current_house = (current_house[0], current_house[1] - 1)
    elif inst == ">":
        current_house = (current_house[0] + 1, current_house[1])
    elif inst == "<":
        current_house = (current_house[0] - 1, current_house[1])
    gifted_houses.add(current_house)

print(len(gifted_houses))
