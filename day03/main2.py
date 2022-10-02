input = open('input.txt')
i1 = 0
j1 = 0
i2 = 0
j2 = 0
l1 = [0]
l2 = [0]
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
    for num in range(len(l1)):
        if (l1[num] == i1 and l2[num] == j1 and count % 2 == 0) or (l1[num] == i2 and l2[num] == j2 and count % 2 != 0):
            flag = -1
            break
    if flag == 0:
        if count % 2 == 0:
            l1.append(i1)
            l2.append(j1)
        else:
            l1.append(i2)
            l2.append(j2)
    count += 1
print(len(l1))
