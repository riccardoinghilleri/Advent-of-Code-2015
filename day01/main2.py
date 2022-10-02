input = open('input.txt')
floor = 0
count = 0
for c in input.readline():
    if c == '(':
        floor += 1
        count += 1
    elif c == ')':
        floor += -1
        count += 1
    if(floor<0):
        break
print(count)
input.close()