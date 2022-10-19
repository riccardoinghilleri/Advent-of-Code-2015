with open('input.txt') as file:
    floor = 0
    for c in file.readline():
        if c == '(':
            floor += 1
        elif c == ')':
            floor += -1
print("Santa is on the " + str(floor) + " floor")
