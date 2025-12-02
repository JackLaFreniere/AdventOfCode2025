with open("Day1/final_input.txt") as f:
    lines = f.readlines()

# Remove the \n on the end of each line
for i in range(len(lines)):
    if i != len(lines) - 1:
        lines[i] = lines[i][:-1]

val = 50
password = 0
for l in lines:
    dir, change = l[0], int(l[1:])
    change = change if dir == "R" else -change

    # I gave up on making a good solution :(
    while change != 0:
        if change > 0:
            val += 1
            change -= 1
        else:
            val -= 1
            change += 1
        
        val %= 100
        if val == 0:
            password += 1

print(password)