from itertools import product

with open('../data/day7.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

test_nums = []
equations = []
for line in input_arr:
    s = line.split(':')
    test_nums.append(int(s[0]))
    equations.append([int(x) for x in s[1].split()])


def solver(num_operators):
    out = []
    for i in range(len(test_nums)):
        binaries = list(product(range(num_operators), repeat=len(equations[i])-1))
        for bin in binaries:
            total = equations[i][0]
            for j in range(len(bin)):
                if bin[j] == 0:
                    total += equations[i][j+1]
                elif bin[j] == 1:
                    total *= equations[i][j+1]
                elif bin[j] == 2:
                    total = int(str(total) + str(equations[i][j+1]))
            if total == test_nums[i]:
                out.append(total)
                break
    return sum(out)


print('Part 1:', solver(2))
print('Part 2:', solver(3))

