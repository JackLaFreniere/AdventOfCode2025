with open("Day2/final_input.txt") as f:
    lines = f.readline().split(",")

for i in range(len(lines)):
    lines[i] = lines[i].strip().split("-")
lines.pop()

sum = 0
for l in lines:
    if len(l[0]) > 1:
        beginning = l[0][0:len(l[0])//2]
    else:
        beginning = l[0]
    while int(beginning * 2) <= int(l[1]):
        if int(beginning * 2) >= int(l[0]):
            diff = int(str(beginning) * 2)
            sum += diff
            print(l, diff)
            if diff == 6161661616:
                print('h')
            
        beginning = str(int(beginning) + 1)
print(sum)