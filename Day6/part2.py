with open("Day6/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = lines[i][:-1]

def evaluate(equation, op):
    num = equation[0]
    if op == "+":
        for x in range(1, len(equation)):
            num += equation[x]
    elif op == "*":
        for x in range(1, len(equation)):
            num *= equation[x]
    
    return num

operations = []
for i in range(len(lines[0])):
    op = ""
    for l in lines:
        op += l[i]
    operations.append(op)

sum = 0
op = ""
equation = []
for i in range(len(operations)):
    o = operations[i]
    if o[-1] == "+" or o[-1] == "*":
        op = operations[i][-1]
        operations[i] = operations[i][:-1]
    operations[i] = operations[i].strip()

    if operations[i] == "":
        sum += evaluate(equation, op)
        equation = []
        op = ""
    else:
        equation.append(int(operations[i]))
sum += evaluate(equation, op)

print(sum)