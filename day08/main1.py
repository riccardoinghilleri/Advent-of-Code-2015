with open('input.txt') as file:
    result_1 = 0
    result_2 = 0
    for line in file:
        line = line.strip('\n')
        string_value_1 = len(line) - 2
        string_value_2 = len(line) + 4
        i = 0
        while i < len(line):
            if (line[i] == '\\') & (i < len(line) - 1):
                if line[i+1] == 'x':
                    string_value_1 -= 3
                    string_value_2 += 1
                    i += 3
                elif line[i+1] == '\\':
                    string_value_1 -= 1
                    string_value_2 += 2
                    i += 1 
                else:
                    string_value_1 -= 1
                    string_value_2 += 2
            i += 1
        result_1 += len(line) - string_value_1
        result_2 += string_value_2 - len(line)
print(result_1)
print(result_2)
