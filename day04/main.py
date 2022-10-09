import hashlib
input = "iwrupvqb"
count = 1
while True:
    result = hashlib.md5((input + str(count)).encode()).hexdigest()
    count += 1
    if result[:6] == "000000":
        count -=1
        break
print(count)