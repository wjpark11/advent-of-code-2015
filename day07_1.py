import re

with open("day07_input.txt", "rt") as f:
    inputs = f.readlines()

instructions = [input.strip().split(" -> ") for input in inputs]

determined_wires = dict()


while "a" not in determined_wires.keys():
    for inst in instructions:
        if re.match(r"^\d+$", inst[0]):
            determined_wires[inst[1]] = int(inst[0])
            instructions.remove(inst)
        elif inst[0].startswith("NOT"):
            operand = inst[0].split(" ")[1]
            if re.match(r"^\d+$", operand):
                determined_wires[inst[1]] = ~int(operand)
                instructions.remove(inst)
            elif operand in determined_wires.keys():
                determined_wires[inst[1]] = ~determined_wires[operand]
                instructions.remove(inst)
        else:
            print(inst[0].split(" "))
            operator = inst[0].split(" ")[1]
            operands = inst[0].split(" ")[0::2]
            if operands[0] in determined_wires.keys() and (
                operands[1] in determined_wires.keys()
                or re.match(r"^\d+$", operands[1])
            ):

                if operator == "AND":
                    determined_wires[inst[1]] = (
                        determined_wires[operands[0]] & determined_wires[operands[1]]
                    )
                    instructions.remove(inst)
                elif operator == "OR":
                    determined_wires[inst[1]] = (
                        determined_wires[operands[0]] | determined_wires[operands[1]]
                    )
                    instructions.remove(inst)
                elif operator == "LSHIFT":
                    determined_wires[inst[1]] = determined_wires[operands[0]] << int(
                        operands[1]
                    )
                    instructions.remove(inst)
                elif operator == "RSHIFT":
                    determined_wires[inst[1]] = determined_wires[operands[0]] >> int(
                        operands[1]
                    )
                    instructions.remove(inst)


print(determined_wires["a"])
