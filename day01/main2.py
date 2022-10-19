floor = count = 0
with open('input.txt') as file:
    for c in file.readline():
        if c == '(':
            floor += 1
            count += 1
        elif c == ')':
            floor += -1
            count += 1
        if floor < 0:
            break
print(count)
