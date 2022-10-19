instructions = []
a = 0
b = 0
count = 0
with open('input.txt') as file:
    for line in file:
        instructions.append(line.split())
while count < len(instructions):
    if (instructions[count])[0] == "hlf":
        if (instructions[count])[1] == 'a':
            a /= 2
        elif (instructions[count])[1] == 'b':
            b /= 2
        count += 1
    elif (instructions[count])[0] == "tpl":
        if (instructions[count])[1] == 'a':
            a *= 3
        elif (instructions[count])[1] == 'b':
            b *= 3
        count += 1
    elif (instructions[count])[0] == "inc":
        if (instructions[count])[1] == 'a':
            a += 1
        elif (instructions[count])[1] == 'b':
            b += 1
        count += 1
    elif (instructions[count])[0] == "jmp" and count + int((instructions[count])[1]) > 0:
        count += int((instructions[count])[1])
    elif (instructions[count])[0] == "jie" and count + int((instructions[count])[2]) > 0:
        if ((instructions[count])[1] == "a," and (a % 2 == 0)) or ((instructions[count])[1] == "b," and b % 2 == 0):
            count += int((instructions[count])[2])
        else:
            count += 1
    elif (instructions[count])[0] == "jio" and count + int((instructions[count])[2]) > 0:
        if ((instructions[count])[1] == 'a,' and a == 1) or ((instructions[count])[1] == 'b,' and b == 1):
            count += int((instructions[count])[2])
        else:
            count += 1
    else:
        break
print(b)
