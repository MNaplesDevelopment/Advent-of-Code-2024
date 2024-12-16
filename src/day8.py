with open('../data/day8.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()
x, y = len(input_arr), len(input_arr[0])

antenna_locs = {}
for i, line in enumerate(input_arr):
    for j, char in enumerate(line):
        if char == '.': continue
        if char in antenna_locs.keys():
            antenna_locs[char].append((i, j))
        else:
            antenna_locs[char] = [(i, j)]


def valid_index(loc):
    return 0 <= loc[0] < x and 0 <= loc[1] < y


antinodes = []
antinodes2 = []
part1 = 0
for antenna in antenna_locs.keys():
    locs = antenna_locs[antenna]
    for i, loc in enumerate(locs):
        for j in range(len(locs)):
            if i == j: continue
            distance = (loc[0] - locs[j][0], loc[1] - locs[j][1])
            antinode = (locs[j][0] - distance[0], locs[j][1] - distance[1])
            if valid_index(antinode):
                if antinode not in antinodes:
                    antinodes.append(antinode)
                    antinodes2.append(antinode)
                while True:
                    antinode = (antinode[0] - distance[0], antinode[1] - distance[1])
                    if not valid_index(antinode): break
                    if antinode not in antinodes2:
                        antinodes2.append(antinode)

for antenna in antenna_locs.keys():
    locs = antenna_locs[antenna]
    if len(locs) > 1:
        for loc in locs:
            if loc not in antinodes2:
                antinodes2.append(loc)


print('Part 1:', len(antinodes))
print('Part 2:', len(set(antinodes2)))








