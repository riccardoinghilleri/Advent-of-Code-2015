result = 0
with open('input.txt') as file:
    for line in file:
        line = line.split('x')
        line[2] = line[2].strip('\n')
        l = [int(line[0]) * int(line[1]), int(line[0]) * int(line[2]), int(line[2]) * int(line[1])]
        result += l[0]*2 + l[1]*2 + l[2]*2 + int(min(l))
print("Wrapping paper: " + str(result))
