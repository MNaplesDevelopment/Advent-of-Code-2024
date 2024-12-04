import numpy as np
import re

with open('../data/day4.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

lines = []
for line in input_arr:
    lines.append([c for c in line])
lines = np.asarray(lines)

diagonals = [lines[::-1, :].diagonal(i) for i in range(-lines.shape[0]+1, lines.shape[1])]
diagonals.extend(lines.diagonal(i) for i in range(lines.shape[1]-1, -lines.shape[0], -1))
diagonals = [n.tolist() for n in diagonals]
diagonals = [''.join(x) for x in diagonals]

part1 = 0
for i in range(lines.shape[0]):
    row = ''.join(lines[i, :])
    column = ''.join(lines[:, i])

    part1 += len(re.findall(r"XMAS", row))
    part1 += len(re.findall(r"XMAS", column))
    part1 += len(re.findall(r"XMAS", row[::-1]))
    part1 += len(re.findall(r"XMAS", column[::-1]))

for diagonal in diagonals:
    part1 += len(re.findall(r"XMAS", diagonal))
    part1 += len(re.findall(r"XMAS", diagonal[::-1]))

print('Part 1:', part1)

part2 = 0
for i in range(lines.shape[0]-2):
    for j in range(lines.shape[1]-2):
        window = lines[i:i+3, j:j+3]
        d1 = ''.join(window.diagonal())
        d2 = ''.join(np.fliplr(window).diagonal())
        if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'):
            part2 += 1

print('Part 2:', part2)




