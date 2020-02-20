x = []
for i in range(int(input())):
    k = list(map(str, input().split()))
    k[0] = int(k[0])
    x.append(k)
x.sort(key = lambda a:(a[0]))
for i in range(len(x)): print('%d %s'%(x[i][0], x[i][1]))