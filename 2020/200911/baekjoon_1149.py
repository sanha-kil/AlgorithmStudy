'''
    백준 1149번 RGB거리 문제
'''

import sys

n = int(sys.stdin.readline())
res = []

for i in range(n):
    res.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    res[i][0] = res[i][0] + min(res[i-1][1], res[i-1][2])
    res[i][1] = res[i][1] + min(res[i-1][0], res[i-1][2])
    res[i][2] = res[i][2] + min(res[i-1][0], res[i-1][1])

print(min(res[n-1]))