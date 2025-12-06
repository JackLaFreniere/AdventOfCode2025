with open("Day6/final_input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "\n" in lines[i]:
            lines[i] = lines[i][:-1]
        lines[i] = lines[i].strip().split()

sum = 0
for i in range(len(lines[0])):
    nums = []
    for l in lines:
        nums.append(l[i])
    op = nums.pop(-1)
    nums = [int(x) for x in nums]

    total = nums[0]
    if op == "+":
        for i in range(1, len(nums)):
            total += nums[i]
    elif op == "*":
        for i in range(1, len(nums)):
            total *= nums[i]
    
    sum += total

print(sum)