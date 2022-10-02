input = open('input.txt')
i = 0
j = 0
l1 = [0]
l2 = [0]
flag = 0
for c in input.readline():
    flag = 0
    if c == '^':
        i -= 1
    elif c == 'v':
        i += 1
    elif c == '<':
        j -= 1
    elif c == '>':
        j += 1
    for num in range(len(l1)):
        if l1[num] == i and l2[num] == j:
            flag = -1
            break
    if flag == 0:
        l1.append(i)
        l2.append(j)
print(len(l1))
