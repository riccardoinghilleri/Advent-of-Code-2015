ribbon = 0
with open('input.txt') as file:
    for line in file:
        line = line.split('x')
        line[2] = line[2].strip('\n')
        l = [int(line[0]) + int(line[1]), int(line[0]) + int(line[2]), int(line[2]) + int(line[1])]
        ribbon += 2 * int(min(l)) + int(line[0]) * int(line[1]) * int(line[2])
print("Ribbon: " + str(ribbon))
