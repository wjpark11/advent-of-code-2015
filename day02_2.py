with open("day02_input.txt", "rt") as f:
    inputs = f.readlines()

demensions = [sorted(list(map(int, line.strip().split("x")))) for line in inputs]


def get_ribbon_length(dimension: list[int]) -> int:
    return (
        2 * (dimension[0] + dimension[1]) + dimension[0] * dimension[1] * dimension[2]
    )


sum = 0
for dimension in demensions:
    sum += get_ribbon_length(dimension)

print(sum)
