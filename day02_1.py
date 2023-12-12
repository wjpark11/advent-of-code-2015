with open("day02_input.txt", "rt") as f:
    inputs = f.readlines()

demensions = [sorted(list(map(int, line.strip().split("x")))) for line in inputs]


def get_wrapping_paper(dimension: list[int]) -> int:
    return (
        (dimension[0] + dimension[1] + dimension[2]) ** 2
        - (dimension[0] ** 2 + dimension[1] ** 2 + dimension[2] ** 2)
        + dimension[0] * dimension[1]
    )


sum = 0
for dimension in demensions:
    sum += get_wrapping_paper(dimension)

print(sum)
