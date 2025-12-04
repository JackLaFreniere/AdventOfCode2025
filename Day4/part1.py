with open("Day4/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = lines[i][:-1]

def get_adjacent(y, x, lines):
    dirs = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    adjacent = 0
    for dir in dirs:
        ny = y + dir[1]
        nx = x + dir[0]
        if nx >= 0 and nx < len(lines[0]) and ny >= 0 and ny < len(lines):
            if lines[ny][nx] == "@" or lines[ny][nx] == "x":
                adjacent += 1
    
    return adjacent

score = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "@" and get_adjacent(y, x, lines) < 4:
            score += 1
            lines[y] = lines[y][:x] + "x" + lines[y][x + 1:]

print(score)