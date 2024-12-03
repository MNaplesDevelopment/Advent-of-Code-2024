import re

with open('../data/day3.txt', 'r') as f:
    file = f.read()

part1, part2 = 0, 0
matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", file)
enabled = True

for match in matches:
    if match == 'do()':
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        s = match.split(',')
        num1 = int(s[0].split('(')[1])
        num2 = int(s[1].split(')')[0])
        part1 += num1 * num2
        if enabled:
            part2 += num1 * num2

print('Part1', part1)
print('Part2', part2)


