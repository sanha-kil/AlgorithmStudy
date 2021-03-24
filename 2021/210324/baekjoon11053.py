import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            k[i] = max(k[i], k[j]+1)

print(k)
print(max(k))
