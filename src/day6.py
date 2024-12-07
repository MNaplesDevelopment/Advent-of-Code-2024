import copy
from tqdm import tqdm

with open('../data/day6.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

maze = []
xy = []

for i, line in enumerate(input_arr):
    maze.append([])
    for j, char in enumerate(line):
        if char == '^':
            xy = [i, j]
        maze[i].append([char, False, -1])  # char, visited, direction

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # Up, Right, Down, Left
H, W = len(maze[0]), len(maze)


def is_valid(modded_maze):
    exploring = True
    direction = 0
    x, y = xy
    while exploring:
        if modded_maze[x][y][1] and modded_maze[x][y][2] == direction:
            return modded_maze, True
        if (x + directions[direction][0] == -1) or (y + directions[direction][1] == -1):
            return modded_maze, False
        modded_maze[x][y][1] = True
        modded_maze[x][y][2] = direction
        x += directions[direction][0]
        y += directions[direction][1]
        if not (0 <= x < H-1 and 0 <= y < W-1):
            modded_maze[x][y][1] = True
            exploring = False
        elif modded_maze[x + directions[direction][0]][y + directions[direction][1]][0] == '#':
            direction = (direction + 1) % 4
            if modded_maze[x + directions[direction][0]][y + directions[direction][1]][0] == '#':
                direction = (direction + 1) % 4
    return modded_maze, False


part1 = 0
m2 = copy.deepcopy(maze)
for line in is_valid(m2)[0]:
    for arr in line:
        part1 += 1 if arr[1] else 0

print('Part 1:', part1)

part2 = 0
for i in tqdm(range(len(maze))):
    for j in range(len(maze[i])):
        if m2[i][j][1] and m2[i][j][0] == '.':
            m = copy.deepcopy(maze)
            m[i][j][0] = '#'
            part2 += 1 if is_valid(m)[1] else 0

print('Part 2:', part2)



