# 백준 1300번 문제 K번째 수

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
left, right = 1, k

while left <= right:
  mid = (left + right) // 2
  idx = 0

  for i in range(1, n+1):
    idx += min(mid//i, n)

  if idx >= k:
    ans = mid
    right = mid -1
  else:
    left = mid + 1

print(ans)