import numpy as np

with open('../data/day1.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

left, right, right_dict = [], [], {}
for line in input_arr:
    s = line.split()
    left.append(int(s[0]))
    r = int(s[1])
    right.append(r)
    if r in right_dict.keys():
        right_dict[r] += 1
    else:
        right_dict[r] = 1

# Part 1
left, right = np.sort(np.asarray(left)), np.sort(np.asarray(right))
distances = np.abs(left - right)
print('Part 1:', np.sum(distances))

# Part 2
similarities = []
for num in left:
    if num in right_dict.keys():
        similarities.append(num * right_dict[num])

print('Part 2:', sum(similarities))
















