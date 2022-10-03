count = 0
with open('input.txt') as input:
    for line in input.readlines():
        vowes = 0
        double_flag = False
        notValid_flag = False
        for num in range(len(line)):
            if line[num:min(num + 2,len(line) - 1)] == "ab" or line[num:min(num + 2,len(line) - 1)] == "cd" or line[num:min(num + 2,len(line) - 1)] == "pq" or line[num:min(num + 2,len(line) - 1)] == "xy":
                notValid_flag = True
                continue
            if line[num] == 'a' or line[num] == 'e' or line[num] == 'i' or line[num] == 'o' or line[num] == 'u':
                vowes += 1
            if num < len(line) - 1 and line[num] == line[num + 1]:
                double_flag = True
        if not notValid_flag and double_flag and vowes >= 3:
            count +=1
print(count)