with open("Day1/input.txt") as f:
    lines = f.readlines()
    lines = [l[:len(l) - 1] for l in lines]

val = 50
password = 0
for l in lines:
    if l[0] == "R":
        val += int(l[1:])
    else:
        val -= int(l[1:])
    val %= 100
    if val == 0:
        password += 1

print(password)