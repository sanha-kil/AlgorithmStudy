import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
  n, m = map(int, input().split())
  weight = deque(list(map(int, input().split())))
  idx = deque([i for i in range(n)])
  answer = []

  while weight:
    if weight[0] == max(weight):
      weight.popleft()
      answer.append(idx.popleft())
    else:
      weight.append(weight.popleft())
      idx.append(idx.popleft())
  
  print(answer.index(m)+1)

