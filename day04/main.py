import hashlib
input = "iwrupvqb"
flag = True
count = 1
while flag:
    flag = False
    result = hashlib.md5((input + str(count)).encode()).hexdigest()
    count += 1
    for num in range(6):
        if result[num] != '0':
            flag = True
    if not flag:
        count -=1
print(count)