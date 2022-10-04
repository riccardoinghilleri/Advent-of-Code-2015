import numpy as np
def toggle(submatrix):
    for i in range(submatrix.shape[0]):
        for j in range(submatrix.shape[1]):
            if submatrix[i,j] == 0:
                submatrix[i,j] = 1
            else:
                submatrix[i,j] = 0
all_lights = np.zeros((1000,1000)) 
on_lights = 0
with open('input.txt') as input:
    for line in input.readlines():
        line = line.split()
        if line[0] == "toggle":
            submatrix = all_lights[int((line[1].split(','))[0]):int((line[3].split(','))[0]) + 1, int((line[1].split(','))[1]):int((line[3].split(','))[1]) + 1]
            toggle(submatrix)
        else:
            submatrix = all_lights[int((line[2].split(','))[0]):int((line[4].split(','))[0]) + 1, int((line[2].split(','))[1]):int((line[4].split(','))[1]) + 1]
            if line[1] == "on":
                submatrix.fill(1)
            elif line[1] == "off":
                submatrix.fill(0)
for i in range(1000):
    for j in range(1000):
        if all_lights[i,j] == 1:
            on_lights +=1
print(on_lights)