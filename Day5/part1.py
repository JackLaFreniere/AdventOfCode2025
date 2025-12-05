with open("Day5/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = lines[i][:-1]

ranges = []
index = lines.index("")
for i in range(index):
    ranges.append([int(x) for x in lines[i].split("-")])

ids = []
for i in range(index + 1, len(lines)):
    ids.append(int(lines[i]))

sum = 0
for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            sum += 1
            break

print(sum)