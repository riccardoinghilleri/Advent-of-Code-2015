import numpy as np
def function(submatrix, x):
    for i in range(submatrix.shape[0]):
        for j in range(submatrix.shape[1]):
            if x > 0:
                submatrix[i,j] += x
            else:
                submatrix[i,j] = max(submatrix[i,j] + x, 0)
all_lights = np.zeros((1000,1000)) 
total_brightness = 0
with open('input.txt') as input:
    for line in input.readlines():
        line = line.split()
        if line[0] == "toggle":
            submatrix = all_lights[int((line[1].split(','))[0]):int((line[3].split(','))[0]) + 1, int((line[1].split(','))[1]):int((line[3].split(','))[1]) + 1]
            function(submatrix, 2)
        else:
            submatrix = all_lights[int((line[2].split(','))[0]):int((line[4].split(','))[0]) + 1, int((line[2].split(','))[1]):int((line[4].split(','))[1]) + 1]
            if line[1] == "on":
                function(submatrix, 1)
            elif line[1] == "off":
                function(submatrix, -1)
for i in range(1000):
    for j in range(1000):
        total_brightness += all_lights[i,j]
print(total_brightness)