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
            if lines[ny][nx] == "@":
                adjacent += 1
    
    return adjacent

score = 0
p_score = 0
while score == 0 or p_score != score:
    p_score = score
    remove = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@" and get_adjacent(y, x, lines) < 4:
                score += 1
                remove.append((x, y))
        
    for r in remove:
        x = r[0]
        y = r[1]
        lines[y] = lines[y][:x] + "x" + lines[y][x + 1:]

print(score)