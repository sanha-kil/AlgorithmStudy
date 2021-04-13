import sys
import math
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
  num.append(int(input()))

num.sort()

arr = []
for i in range(1, n):
  arr.append(num[i]-num[i-1])

tmp = arr[0]
for i in range(len(arr)):
  tmp = math.gcd(tmp, arr[i])

ans = [tmp]
for i in range(2, int(tmp**0.5)+1):
  if tmp % i == 0:
    ans.append(i)
    ans.append(tmp//i)

ans.sort()
ans = list(set(ans))

for x in ans:
  print(x, end=' ')