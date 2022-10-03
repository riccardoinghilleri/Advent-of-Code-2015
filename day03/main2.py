class House:
    def __init__(self,i,j):
        self.i = i
        self.j = j

input = open('input.txt')
i1 = 0
j1 = 0
i2 = 0
j2 = 0
l1 = [House(0,0)]
flag = 0
count = 0
for c in input.readline():
    flag = 0
    if count % 2 == 0:
        if c == '^':
            i1 -= 1
        elif c == 'v':
            i1 += 1
        elif c == '<':
            j1 -= 1
        elif c == '>':
            j1 += 1
    else:
        if c == '^':
            i2 -= 1
        elif c == 'v':
            i2 += 1
        elif c == '<':
            j2 -= 1
        elif c == '>':
            j2 += 1
    for elem in l1:
        if (elem.i == i1 and elem.j == j1 and count % 2 == 0) or (elem.i == i2 and elem.j == j2 and count % 2 != 0):
            flag = -1
            break
    if flag == 0:
        if count % 2 == 0:
            l1.append(House(i1,j1))
        else:
            l1.append(House(i2,j2))
    count += 1
print(len(l1))
