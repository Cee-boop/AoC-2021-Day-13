with open(file='data.txt') as file:
    data = file.read().split("\n")
    coords = data[:-13]
    folds = data[-12:]

max_y, max_x = float('-inf'), float('-inf')
for coord in coords:
    x, y = map(int, coord.split(","))
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y


def display_grid():
    global grid
    s = [[str(e) for e in row] for row in grid]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def visible_dots(curr_step):
    global grid
    dots = 0
    for line in grid:
        dots += line.count('#')
    return print(f"current step: {curr_step + 1}, dot count: {dots}")


def horizontal_fold(fold_line):
    global grid
    for y, row in enumerate(grid[::-1]):
        for x, col in enumerate(row):
            if grid[::-1][y][x] == "#":
                grid[y][x] = "#"

    grid = grid[:fold_line]


def vertical_fold(fold_line):
    global grid
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if grid[y][x] == "#":
                new_pos = (len(row) - 1) - x
                grid[y][new_pos] = "#"

    grid = [line[:fold_line] for line in grid]


grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for coord in coords:
    x, y = map(int, coord.split(","))
    grid[y][x] = "#"

for step, entry in enumerate(folds):
    curr_fold = entry.split("=")
    coord, number = curr_fold[0][-1], int(curr_fold[-1])
    if coord == "x":
        vertical_fold(number)
    else:
        horizontal_fold(number)

    visible_dots(step)
    display_grid()
