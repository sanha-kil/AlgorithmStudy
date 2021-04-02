import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(int(input()))

count = 0
arr.sort(reverse=True)

for i in range(n):
  if k==0:
    break
  elif arr[i]>k:
    continue
  else:
    count += k//arr[i]
    k %= arr[i]

print(count)