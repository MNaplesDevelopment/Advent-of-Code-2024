with open('../data/day6.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

maze = []
visited = []
x = y = 0
for i, line in enumerate(input_arr):
    chars = []
    for j, char in enumerate(line):
        if char == '^':
            x, y = i, j
        chars.append(char)
    maze.append(chars)
    visited.append([False]*len(chars))

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # Up, Right, Down, Left
H, W = len(maze[0]), len(maze)
exploring = True
direction = 0
while exploring:
    visited[x][y] = True
    x += directions[direction][0]
    y += directions[direction][1]
    if not (0 <= x < H-1 and 0 <= y < W-1):
        visited[x][y] = True
        exploring = False
    elif maze[x + directions[direction][0]][y + directions[direction][1]] == '#':
        direction = (direction + 1) % 4

part1 = 0
for line in visited:
    part1 += sum(line)

print('Part 1:', part1)







