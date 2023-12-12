import re

with open("day25_input.txt", "rt") as f:
    inputs = f.readlines()

instruction = [input.strip() for input in inputs][0]
[ROW, COL] = [int(x) for x in re.findall(r"\d+", instruction)]

group_num = ROW + COL - 1
group_start_num = (group_num - 1) * group_num // 2 + 1
sequence_num = group_start_num + COL - 1


def next_code(code):
    return (code * 252533) % 33554393


code = 20151125
for _ in range(sequence_num - 1):
    code = next_code(code)

print(code)
