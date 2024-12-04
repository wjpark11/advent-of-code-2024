with open("day04_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


# Part 1
def count_xmas(inputs: list[list], position: tuple[int]) -> int:
    input_width = len(inputs[0])
    input_height = len(inputs)
    def check_index(x: int, y: int) -> bool:
        if (x < 0 or x >= input_width) or (y < 0 or y >= input_height):
            return False
        return True

    x, y = position
    count = 0
    if check_index(x+3, y) and [inputs[x+i][y] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x-3, y) and [inputs[x-i][y] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x, y+3) and [inputs[x][y+i] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x, y-3) and [inputs[x][y-i] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x+3, y+3) and [inputs[x+i][y+i] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x-3, y-3) and [inputs[x-i][y-i] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x+3, y-3) and [inputs[x+i][y-i] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    if check_index(x-3, y+3) and [inputs[x-i][y+i] for i in range(4)] == ["X", "M", "A", "S"]:
        count += 1
    return count


def part1(inputs: list[str]) -> int:
    total_xmas_count = 0
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            total_xmas_count += count_xmas(inputs, (i, j))
    return total_xmas_count


# Part 2
def part2(inputs: list[str]) -> int:
    input_width = len(inputs[0])
    input_height = len(inputs)
    xmas_count = 0
    def check_index(x: int, y: int) -> bool:
        if (x-1 < 0 or x+1 >= input_width) or (y-1 < 0 or y+1 >= input_height):
            return False
        return True
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if check_index(i, j) and inputs[i][j] == "A" and {inputs[i-1][j-1] , inputs[i+1][j+1]} == {"M", "S"} and {inputs[i-1][j+1], inputs[i+1][j-1]} == {"M", "S"}:
                xmas_count += 1
    return xmas_count



if __name__ == "__main__":
    print(part1(inputs))
    print(part2(inputs))