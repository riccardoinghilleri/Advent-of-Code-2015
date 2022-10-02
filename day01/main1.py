input = open('input.txt')
floor = 0
for c in input.readline():
    if c == '(':
        floor += 1
    elif c == ')':
        floor += -1
print("Santa is on the " + str(floor) + " floor")
input.close()