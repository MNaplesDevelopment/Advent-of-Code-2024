with open('../data/day5.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

rules = {}
pages = []
for line in input_arr:
    if '|' in line:
        s1, s2 = line.split('|')
        s1, s2 = int(s1), int(s2)
        if s1 in rules.keys():
            rules[s1].append(s2)
        else:
            rules[s1] = [s2]
    elif line == '':
        continue
    else:
        pages.append([int(x) for x in line.split(',')])


def is_valid(page):
    for i in range(len(page)):
        for key in page[i:]:
            if key not in rules.keys():
                continue
            if page[i] in rules[key]:
                return False, page[i], key
    return True, None, None


def separate_correct_incorrect(pages):
    correct = []
    incorrect = []
    for page in pages:
        if is_valid(page)[0]:
            correct.append(page)
        else:
            incorrect.append(page)
    return correct, incorrect


part1 = 0
correct, wrong = separate_correct_incorrect(pages)
for c in correct:
    part1 += c[len(c) // 2]
print('Part 1:', part1)

part2 = 0
ans = []
for w in wrong:
    page = w.copy()
    valid, num1, num2 = is_valid(page)
    while not valid:
        idx1 = page.index(num1)
        idx2 = page.index(num2)
        page[idx1], page[idx2] = page[idx2], page[idx1]
        valid, num1, num2 = is_valid(page)
    ans.append(page)

for c in ans:
    part2 += c[len(c) // 2]
print('Part 2:', part2)

