x = []
for i in range(int(input())):
    k = input()
    x.append([k, len(k)])
x = list(set(map(tuple, x)))
x.sort(key = lambda a:(a[1], a[0]))
for i in range(len(x)): print(x[i][0])