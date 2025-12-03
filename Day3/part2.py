import itertools

with open("Day3/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i != len(lines) - 1:
            lines[i] = lines[i][:-1]
   
def biggest_num(sequence):
    biggest = int(sequence[0])
    for s in sequence:
        if int(s) > biggest:
            biggest = int(s)
    return sequence.index(str(biggest))

sum = 0
for l in lines:
    max_num = ""

    offset = 0
    for i in range(12):
        i += offset
        size = len(l) - 12 + 1 - offset
        sequence = l[i:i + size]
        biggest_index = biggest_num(sequence)
        offset += biggest_index
        max_num += l[i + biggest_index]

    sum += int(max_num)
    print(max_num)

print(sum)