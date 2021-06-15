# 백준 2805번 문제 "나무 자르기"

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

l, h = 0, max(tree)

while l <= h:
  mid = (l+h)//2
  leng = 0
  for t in tree:
    if t > mid:
      leng += t - mid
  
  if leng < m:
    h = mid - 1
  else:
    l = mid + 1

print(h)