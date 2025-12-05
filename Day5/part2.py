with open("Day5/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = lines[i][:-1]

ranges = []
index = lines.index("")
for i in range(index):
    ranges.append([int(x) for x in lines[i].split("-")])

def in_any_range(num):
    global ranges
    for r in ranges:
        if num >= r[0] and num <= r[1]:
            return True
    return False

# Get all values of endpoints in ranges
sum = 0
indexes = []
for r in ranges:
    indexes.append(r[0])
    indexes.append(r[1])
indexes = sorted(set(indexes)) # Remove duplicates

# Check inbetween start and endpoints to see if an invalid id exists
# If so, sum up the sizes of every invalid id range. 
size = indexes[-1] + 1 - indexes[0]
for i in range(len(indexes)- 1):
    val = indexes[i] + 1
    if not in_any_range(val):
        sum += indexes[i + 1] - indexes[i] - 1

# Print the maximum possible size of ranges minus the invalid ones for all valid ids
print(size - sum)