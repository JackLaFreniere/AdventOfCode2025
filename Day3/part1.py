with open("Day3/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i != len(lines) - 1:
            lines[i] = lines[i][:-1]

sum = 0
for l in lines:
    max_num = 0

    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if i >= j:
                continue
            
            num = int(l[i] + l[j])

            if num > max_num:
                max_num = num

    sum += max_num

print(sum)