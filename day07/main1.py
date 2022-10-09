def search(string, signals):
    for elem in signals:
        if elem[len(elem)-1] == string:
            index = signals.index(elem)
            break
    if len(signals[index]) == 3 and (signals[index])[0].isdigit():
        return (signals[index])[0]
    elif len(signals[index]) == 3:
        return search((signals[index])[0], signals)
    elif (signals[index])[0] == "NOT" and len(signals[index]) == 4:
        if type((signals[index])[1]) is not int and not (signals[index])[1].isdigit():
            (signals[index])[1] = search((signals[index])[1], signals)
        return ~ int((signals[index])[1])
    elif len(signals[index]) == 5:
        if type((signals[index])[0]) is not int and not (signals[index])[0].isdigit():
                (signals[index])[0] = search((signals[index])[0], signals)
        if type((signals[index])[2]) is not int and not (signals[index])[2].isdigit():
            (signals[index])[2] = search((signals[index])[2], signals)
        if (signals[index])[1] == "OR":
            return int((signals[index])[0]) | int((signals[index])[2])
        elif (signals[index])[1] == "AND":
            return int((signals[index])[0]) & int((signals[index])[2])
        elif (signals[index])[1] == "LSHIFT":
            return int((signals[index])[0]) << int((signals[index])[2])
        elif (signals[index])[1] == "RSHIFT":
            return int((signals[index])[0]) >> int((signals[index])[2])


with open('input.txt') as input:
    signals = []
    for line in input.readlines():
        signals.append(line.split())
    print(search('a', signals))