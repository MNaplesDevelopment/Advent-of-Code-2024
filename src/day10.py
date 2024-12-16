with open('../data/day10.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()
maze = []
for line in input_arr:
    maze.append([int(c) for c in line])

visited = []
part1_bool = True


def path_finder(path):
    if part1_bool:
        if path in visited:
            return 0
    x, y = path
    visited.append(path)
    if maze[x][y] == 9:
        return 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    # Remove invalid directions
    if x == 0:
        directions.remove((-1, 0))
    elif x == len(maze)-1:
        directions.remove((1, 0))
    if y == 0:
        directions.remove((0, -1))
    elif y == len(maze[0])-1:
        directions.remove((0, 1))

    # Find valid paths for each direction
    paths = []
    for direction in directions:
        dx = x + direction[0]
        dy = y + direction[1]
        if maze[dx][dy] - maze[x][y] == 1:
            paths.append((dx, dy))

    length = len(paths)
    if length == 0:
        return 0
    elif length == 1:
        return path_finder(paths[0])
    elif length == 2:
        return path_finder(paths[0]) + path_finder(paths[1])
    elif length == 3:
        return path_finder(paths[0]) + path_finder(paths[1]) + path_finder(paths[2])
    elif length == 4:
        return path_finder(paths[0]) + path_finder(paths[1]) + path_finder(paths[2]) + path_finder(paths[3])


part1 = 0
for i, row in enumerate(maze):
    for j, num in enumerate(row):
        if num == 0:
            part1 += path_finder((i, j))
            visited = []
print('Part 1:', part1)

part2 = 0
part1_bool = False
for i, row in enumerate(maze):
    for j, num in enumerate(row):
        if num == 0:
            part2 += path_finder((i, j))
print('Part 2:', part2)
