with open('../data/day2.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

lines = []
for line in input_arr:
    s = line.split()
    lines.append([int(x) for x in s])


def is_safe(arr):
    ascending = (arr[0] - arr[1]) > 0
    for i in range(1, len(arr)):
        diff = arr[i-1] - arr[i]
        diff_asc = diff > 0
        diff = abs(diff)
        if diff_asc is not ascending:
            return False
        if not (1 <= diff <= 3):
            return False
    return True


part1 = 0
part2 = 0
for line in lines:
    if is_safe(line):
        part1 += 1
        part2 += 1
        continue
    for j in range(len(line)):
        copy = line.copy()
        copy.pop(j)
        if is_safe(copy):
            part2 += 1
            break

print('Part 1:', part1)
print('Part 2:', part2)
