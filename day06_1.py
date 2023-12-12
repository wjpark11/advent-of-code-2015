import re

with open("day06_input.txt", "rt") as f:
    inputs = f.readlines()


def parse_input(line: str) -> dict:
    instruction = dict()
    if line.startswith("turn on"):
        instruction["action"] = "on"
    elif line.startswith("turn off"):
        instruction["action"] = "off"
    elif line.startswith("toggle"):
        instruction["action"] = "toggle"

    grid_nums = re.findall(r"\d+", line)
    instruction["start"] = (int(grid_nums[0]), int(grid_nums[1]))
    instruction["end"] = (int(grid_nums[2]), int(grid_nums[3]))

    return instruction


instructions = [parse_input(input.strip()) for input in inputs]

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for inst in instructions:
    if inst["action"] == "on":
        for i in range(inst["start"][0], inst["end"][0] + 1):
            for j in range(inst["start"][1], inst["end"][1] + 1):
                grid[i][j] = 1
    elif inst["action"] == "off":
        for i in range(inst["start"][0], inst["end"][0] + 1):
            for j in range(inst["start"][1], inst["end"][1] + 1):
                grid[i][j] = 0
    elif inst["action"] == "toggle":
        for i in range(inst["start"][0], inst["end"][0] + 1):
            for j in range(inst["start"][1], inst["end"][1] + 1):
                grid[i][j] = 1 - grid[i][j]

print(sum([sum(row) for row in grid]))
