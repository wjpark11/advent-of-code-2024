with open("day01_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]
    inputs = [d.split('   ') for d in inputs]
    inputs = [[int(item) for item in data] for data in inputs]

# Part 1
def part1(inputs: list) -> int:
    list1 = [item[0] for item in inputs]
    list2 = [item[1] for item in inputs]

    list1.sort()
    list2.sort()

    diffs = [abs(a - b) for a, b in zip(list1, list2)]

    return sum(diffs)

# Part 2
def part2(inputs: list) -> int:
    list1 = [item[0] for item in inputs]
    list2 = [item[1] for item in inputs]

    occurences = [list2.count(item) for item in list1]
    similarity_scores = [a * b for a, b in zip(list1, occurences)]

    return sum(similarity_scores)


if __name__ == "__main__":
    print(part1(inputs))
    print(part2(inputs))