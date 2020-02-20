import sys
import math

x = []
for i in range(int(input())):
    x.append(list(map(int, sys.stdin.readline().split())))
y = sorted(x)
for i in range(len(x)): print("%d %d"%(y[i][0],y[i][1]))