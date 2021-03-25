import sys

input = sys.stdin.readline

n = int(input())
arr=[]

for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort()

k = [1]*n

print(arr)

for i in range(1, n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            k[i] = max(k[i], k[j]+1)

print(n-max(k))