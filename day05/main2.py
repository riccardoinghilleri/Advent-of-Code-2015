count = 0
with open('input.txt') as input:
    for line in input.readlines():
        repeat_flag = False
        pair_flag = False
        for num in range(len(line)):
            if num > 0:
                sub = line[num - 1] + line[num]
                if line.count(sub) > 1:
                    pair_flag = True
            if num < len(line) - 2 and line[num] == line[num + 2]:
                repeat_flag = True
        if repeat_flag and pair_flag:
            count +=1
print(count)