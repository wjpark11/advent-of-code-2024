with open("day05_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

blank_line_index = inputs.index('')
rules = [rule.split("|") for rule in inputs[:blank_line_index]]
updates = [update.split(",") for update in inputs[blank_line_index+1:]]


# Part 1
def meet_rule(rule: list[str], update: list[str]) -> bool:
    try:
        rule_1_idx = update.index(rule[0])
        rule_2_idx = update.index(rule[1])
    except ValueError:
        return True

    return rule_1_idx < rule_2_idx


def part1(rules: list[str], updates: list[list[str]]) -> int:
    middle_page_num_sum = 0
    for update in updates:
        if all(meet_rule(rule, update) for rule in rules):
            middle_page_num = update[len(update)//2]
            middle_page_num_sum += int(middle_page_num)

    return middle_page_num_sum


# Part 2
def get_ordered_update(rules: list[str], update: list[str]) -> list[str]:
    related_rules = []
    for rule in rules:
        try:
            rule_1_idx = update.index(rule[0])
            rule_2_idx = update.index(rule[1])
        except ValueError:
            continue
        else:
            related_rules.append(rule)
    print(len(related_rules))


def part2(rules: list[str], updates: list[list[str]]) -> int:
    middle_page_num_sum = 0
    for update in updates:
        if not all(meet_rule(rule, update) for rule in rules):
            get_ordered_update(rules, update)
            print(len(update))
            # ordered_update = get_ordered_update(rules, update)
            # middle_page_num = ordered_update[len(ordered_update)//2]
            # middle_page_num_sum += int(middle_page_num)

    return middle_page_num_sum


if __name__ == "__main__":
    print(part1(rules, updates))
    print(part2(rules, updates))