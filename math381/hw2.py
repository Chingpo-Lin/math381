import math

n = 5
V = []
E = []
color = []

for i in range(1, n + 1):
    V.append(i)
    color.append(i)

'''E = {(i,j): sin(i)+sin(j)<0, 1 ≤ i,j ≤ n}'''
for i in V:
    for j in range(i + 1, n + 1):
        if math.sin(i) + math.sin(j) < 0:
            E.append((i, j))

'''objective function'''
output = "min: "
for i in range(1, n + 1):
    output = output + "+y_" + str(i)
print(output + ";")

'''constraint1'''
for i in range(1, n + 1):
    output1 = ""
    for k in range(1, n + 1):
        output1 = output1 + "+x_" + str(i) + "_" + str(k)
    print(output1 + "=1;")

'''constraint2'''
for k in range(1, n + 1):
    for i in range(1, n + 1):
        print("+x_" + str(i) + "_" + str(k) + "<=y_" + str(k) + ";")

'''constraint3'''
for (i, j) in E:
    for k in range(1, n + 1):
        print("+x_" + str(i) + "_" + str(k) + "+x_" + str(j) + "_" + str(k) + "<=1;")

'''constraint4'''
for k in range(1, n):
    print("y_" + str(k + 1) + "<=y_" + str(k) + ";")

'''constraint5'''
output = "bin "
for k in range(1, n + 1):
    output = output + "y_" + str(k) + ","
    for i in range(1, n):
        output = output + "x_" + str(i) + "_" + str(k) + ","
output = output + "x_" + str(n) + "_" + str(n)
print(output + ";")