with open("day06_input.txt", "rt") as f:
    inputs = f.readlines()
    lab_map = [row.strip() for row in inputs]

MAP_WIDTH = len(lab_map[0])
MAP_HEIGHT = len(lab_map)

guard_position_row = 0