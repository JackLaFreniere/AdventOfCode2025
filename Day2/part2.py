for i in range(2):
    if i == 0:
        with open("Day2/test_input.txt") as f:
            lines = f.readline().split(",")
    else:
        with open("Day2/final_input.txt") as f:
            lines = f.readline().split(",")

    for i in range(len(lines)):
        lines[i] = lines[i].strip().split("-")
        lines[i][0] = int(lines[i][0])
        lines[i][1] = int(lines[i][1])

    # I'm gonna crash out I couldn't figure out how to create all invalid id's from the ranges
    # so I just searched through all possible id's inbetween the ranges and identified the invalid ones
    sum = 0
    for l in lines:
        vals = list(range(l[0], l[1] + 1))
        ids = []
        for val in vals:
            length = 1
            while length <= len(str(val)) / 2:
                items = []
                offset = 0
                while offset < len(str(val)):
                    value = str(val)[offset:offset + length]
                    items.append(value)
                    offset += length
                length += 1

                wrong = False
                for item in items:
                    if item != items[0]:
                        wrong = True
                
                if not wrong:
                    sum += val
                    print(l, val)
                    break

    print(sum)