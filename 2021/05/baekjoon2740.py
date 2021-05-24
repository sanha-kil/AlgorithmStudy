import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))


#행렬 곱셈
C = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            C[i][j] += A[i][l] * B[l][j]

#출력문
for i in C:
    for j in i:
        print(j, end = ' ')
    print('')