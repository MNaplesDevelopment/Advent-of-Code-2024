import numpy as np
import re

with open('../data/day4.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

lines = []
for line in input_arr:
    lines.append([c for c in line])

lines = np.asarray(lines)
diagonals = [''.join(lines.diagonal()), ''.join(np.flipud(lines).diagonal())]
for i in range(1, lines.shape[0]):
    diagonals.append(''.join(lines.diagonal(offset=i)))
    diagonals.append(''.join(lines.diagonal(offset=-i)))
    diagonals.append(''.join(np.fliplr(lines).diagonal(offset=i)))
    diagonals.append(''.join(np.flipud(lines).diagonal(offset=i)))

total = 0
rows = []
columns = []
for i in range(lines.shape[0]):
    rows.append(''.join(lines[i, :]))
    columns.append(''.join(lines[:, i]))

for i in range(len(rows)):
    matches = re.findall(r"XMAS", rows[i])
    total += len(matches)

    matches = re.findall(r"XMAS", columns[i])
    total += len(matches)

    matches = re.findall(r"XMAS", rows[i][::-1])
    total += len(matches)

    matches = re.findall(r"XMAS", columns[i][::-1])
    total += len(matches)

for x in diagonals:
    matches = re.findall(r"XMAS", x)
    total += len(matches)

    matches = re.findall(r"XMAS", x[::-1])
    total += len(matches)

print(total)

total = 0
y, x = lines.shape
for i in range(y-2):
    for j in range(x-2):
        window = lines[i:i+3, j:j+3]
        d1 = ''.join(window.diagonal())
        d2 = ''.join(np.fliplr(window).diagonal())
        if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'):
            total += 1

print(total)




