import sys
 
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

for i in range(1, len(l)):
    for j in range(len(l[i])):
        if j == 0:
            l[i][j] = l[i][j] + l[i-1][j]
        elif len(l[i])-1 == j:
            l[i][j] = l[i][j] + l[i-1][j-1]
        else:
            l[i][j] = l[i][j] + max(l[i-1][j-1], l[i-1][j])

print(max(l[n-1]))
'''
    백준 1932번 정수삼각형 문제
'''