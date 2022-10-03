class House:
    def __init__(self,i,j):
        self.i = i
        self.j = j

input = open('input.txt')
i = 0
j = 0
flag = 0
l1 = [House(i,j)]
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
    for elem in l1:
        if elem.i == i and elem.j == j:
            flag = -1
            break
    if flag == 0:
        l1.append(House(i,j))
print(len(l1))


