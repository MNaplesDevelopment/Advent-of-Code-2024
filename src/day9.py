from tqdm import tqdm

with open('../data/day9test.txt', 'r') as f:
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
        disk2.append(str(page_id) * num)
        for _ in range(num):
            disk.append(str(page_id))
        page_id += 1
    dot = not dot

for i in tqdm(range(len(disk))):
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

print(part1)

for i in range(len(disk2)-1, 0, -1):
    if not disk[i].isnumeric(): continue
    for j in range(1, len(disk2)):
        if '.' in disk2[j] and len(disk2[j]) >= len(disk[i]):
            disk2.insert(j+1, '.' * (len(disk[i]) - len(disk2[j])))
            disk2[j] = disk2[i]
            del disk2[i]
            break

print(disk2)


# final_str = ''
# t = []
# print(page_ids)
# for i in range(len(page_ids)-1, 0, -1):
#     page = page_ids[i]
#     for j, dot in enumerate(dots):
#         if len(dot) >= len(page):
#             dots[j] = '.' * (len(dot) - len(page))
#             t.append(page)
#             page_ids.insert(j+1, page_ids.pop(i))
#             break
#
# print(t)

