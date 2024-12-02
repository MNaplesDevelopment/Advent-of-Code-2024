import numpy as np

with open('../data/day1.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

left, right = [], []
for line in input_arr:
    s = line.split()
    left.append(int(s[0]))
    right.append(int(s[1]))

left, right = np.sort(np.asarray(left)), np.sort(np.asarray(right))

distances = np.abs(left - right)

print('Part 1:', np.sum(distances))

# Part 2

left, right = [], {}
for line in input_arr:
    s = line.split()
    left.append(int(s[0]))
    r = int(s[1])
    if r in right.keys():
        right[r] += 1
    else:
        right[r] = 1

similarities = []
for num in left:
    if num in right.keys():
        similarities.append(num * right[num])

print('Part 2:', sum(similarities))
















