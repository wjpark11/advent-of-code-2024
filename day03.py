import re

with open("day03_input.txt", "rt") as f:
    inputs = f.readlines()
    corrupted_instructions = [input.strip() for input in inputs]
    

# Part 1
def mul(instruction: str) -> int:
    nums = re.search(r"mul\((\d+),(\d+)\)", instruction)
    return int(nums.group(1)) * int(nums.group(2))

def part1(corrupted_instructions: list[str]) -> int:
    add_up = 0
    for corrupted_instruction in corrupted_instructions:
        instructions = re.findall(r"mul\(\d+,\d+\)", corrupted_instruction)
        for instruction in instructions:
            add_up += mul(instruction)
    return add_up


# Part 2
def part2(corrupted_instructions: list[str]) -> int:
    add_up = 0
    instruction_list = []
    for corrupted_instruction in corrupted_instructions:
        instructions = [match[0] for match in re.findall(r"(mul\(\d+,\d+\)|do(n't)?\(\))", corrupted_instruction)]
        instruction_list += instructions
    flag = True
    for inst in instruction_list:
        if inst == r"don't()":
            flag = False
        elif inst == r"do()":
            flag = True
        else:
            if flag:
                add_up += mul(inst)

    return add_up


if __name__ == "__main__":
    print(part1(corrupted_instructions))
    print(part2(corrupted_instructions))