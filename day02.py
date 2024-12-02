with open("day02_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]
    inputs = [d.split(' ') for d in inputs]
    inputs = [[int(item) for item in data] for data in inputs]

# Part 1
def is_safe(report: list[int]) -> bool:

    gaps = [a - b for a, b in zip(report, report[1:])]
    consistency = ["-" if gap > 0 else "+" for gap in gaps]
    if max([abs(gap) for gap in gaps]) > 3 or min([abs(gap) for gap in gaps]) == 0:
        return False
    if len(set(consistency)) == 1:
        return True
    else:
        return False
    

def part1(inputs: list) -> int:
    safe_reports = 0
    for report in inputs:
        if is_safe(report):
            safe_reports += 1
    return safe_reports

# Part 2
def is_safe_if_removing_one(report: list[int]) -> bool:
    if is_safe(report):
        return True
    for i, item in enumerate(report):
        copied_report = report.copy()
        copied_report.pop(i)
        if is_safe(copied_report):
            return True
    return False

def part2(inputs: list) -> int:
    safe_reports = 0
    for report in inputs:
        if is_safe_if_removing_one(report):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    print(part1(inputs))
    print(part2(inputs))


    