# 벡준 2110번 문제 "공유기 설치"

import sys
input =sys.stdin.readline

n, c = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])

min_gap = 1
max_gap = x[-1] - x[0]

while min_gap <= max_gap:
  gap = (min_gap+max_gap)//2
  installed = x[0]
  cnt = 1

  for a in x[1:]:
    if a >= installed + gap:
      installed = a
      cnt+=1
    
  if cnt >= c:
    min_gap = gap + 1
    answer = gap
  else:
    max_gap = gap - 1

print(answer)