import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_rev = arr[::-1]

asc = [1]*n
desc = [1]*n

for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      asc[i] = max(asc[i], asc[j]+1)
    if arr_rev[j] < arr_rev[i]:
      desc[i] = max(desc[i], desc[j]+1)

answer = []
for i in range(n):
  answer.append(asc[i] + desc[n-i-1] - 1)

print(max(answer))