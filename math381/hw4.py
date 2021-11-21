
n = 10
m = 9
time_limit = 15 * m;

bj = [0, 3.17, 2.08, 2.08, 11.8, 16.5, 17.25, 3.92, 14.67, 5.08]
sz = [3.17, 0, 2.25, 8.42, 18.42, 18.75, 22.75, 5.33, 20.08, 7.58]
sh = [2.08, 2.25, 0, 1.75, 12.33, 11.75, 19.25, 5.08, 21, 4.25]
se = [2.08, 8.42, 1.75,	0, 12.17, 11.5,	17.92, 9.25, 14.75,	5.67]
pa = [11.08, 18.42, 12.33, 12.17, 0, 3.72, 7.42, 19.67, 10.25, 15.42]
fr = [16.5, 18.75, 11.75, 11.5, 3.72, 0, 7.67, 22.58, 6.33, 2.08]
mt = [17.25, 22.75, 19.25, 17.92, 7.42, 7.67, 0, 29, 19.42, 20.33]
ur = [3.92, 5.33, 5.08, 9.25, 19.67, 22.58, 29, 0, 19.33, 10.33]
db = [14.67, 20.08, 21,	14.75, 10.25, 6.33, 19.42, 19.33, 0, 6.33]
bk = [5.08, 7.58, 4.25, 5.67, 15.42, 2.08, 20.33, 10.33, 6.33, 0]

rating = [11, 11, 9, 7, 8, 7, 3, 9, 8, 5]
'''start and ending city'''
sj = [18.08, 23.58, 18, 11.42, 12.25, 12.17, 9.92, 25, 22, 17.92]

city = [bj, sz, sh, se, pa, fr, mt, ur, db, bk]

'''objective function'''
output = "max: "
for i in range(1, m + 1):
    for j in range(1, n + 1):
        output = output + "+" + str(rating[j - 1]) + "x_" + str(i) + "_" + str(j)
print(output + ";")

'''constraints 1'''
for i in range(1, m + 1):
    c1 = ""
    for j in range(1, n + 1):
        c1 = c1 + "+" + "x_" + str(i) + "_" + str(j)
    print(c1 + "=1;")

'''constraints 2'''
for j in range(1, n + 1):
    c2 = ""
    for i in range(1, m + 1):
        c2 = c2 + "+" + "x_" + str(i) + "_" + str(j)
    print(c2 + "<=1;")

'''constraints 3'''
for i in range(1, m):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                c3 = ""
                c3 = c3 + "+" + "e_" + str(a) + "_" + str(b)
                c3 = c3 + ">="
                c3 = c3 + "+" + "x_" + str(i) + "_" + str(a)
                c3 = c3 + "+" + "x_" + str(i + 1) + "_" + str(b)
                print(c3 + "-1;")

'''distance bound'''
bound = ""
for a in range(1, n + 1):
    if sj[a - 1] != 0:
        bound = bound + "+" + str(sj[a - 1]) + "x_" + str(m) + "_" + str(a)
        bound = bound + "+" + str(sj[a - 1]) + "x_1" + "_" + str(a)
    for b in range(1, n + 1):
        if a != b:
            bound = bound + "+" + str(city[a - 1][b - 1]) + "e_" + str(a) + "_" + str(b)
print(bound + "<=" + str(time_limit) + ";")

'''variables'''
var = "bin "
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a != b:
            var = var + "e_" + str(a) + "_" + str(b) + ","
for i in range(1, m + 1):
    for j in range(1, n + 1):
        var = var + "x_" + str(i) + "_" + str(j) + ","
var = var + "x_" + str(m) + "_" + str(n)
print(var + ";")
