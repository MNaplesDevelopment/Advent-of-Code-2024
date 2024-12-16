with open('../data/day9.txt', 'r') as f:
    file = f.read()

dot = False
page_id = 0
disk = []
disk2 = []

for i in range(len(file)):
    num = int(file[i])
    if dot:
        disk2.append('.' * num)
        for _ in range(num):
            disk.append('.')
    else:
        disk2.append([str(page_id) for _ in range(num)])
        for _ in range(num):
            disk.append(str(page_id))
        page_id += 1
    dot = not dot

for i in range(len(disk)):
    if disk[i].isnumeric(): continue
    swapped = False
    for j in range(len(disk)-1, i, -1):
        if disk[j].isdigit():
            disk[i], disk[j] = disk[j], disk[i]
            swapped = True
            break
    if not swapped: break

part1 = 0
for i, c in enumerate(disk):
    if c.isdigit():
        part1 += i * int(c)
    else:
        break

print('Part 1:', part1)

for i in range(len(disk2)-1, 0, -1):
    if type(disk2[i]) is str: continue
    for j in range(1, i):
        if '.' in disk2[j] and len(disk2[j]) >= len(disk2[i]):
            diff = len(disk2[j]) - len(disk2[i])
            disk2[j] = disk2[i]
            if diff != 0:
                disk2.insert(j+1, '.' * diff)
                disk2[i+1] = '.' * len(disk2[i+1])
            else:
                disk2[i] = '.' * len(disk2[i])
            break

part2 = 0
page_rank = 0
for chunk in disk2:
    if type(chunk) is str:
        page_rank += len(chunk)
        continue
    for char in chunk:
        part2 += page_rank * int(char)
        page_rank += 1

print('Part 2:', part2)



