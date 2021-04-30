import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([i+1 for i in range(n)])
count = 0

for i in range(m):
  if len(que)/2 > que.index(arr[i]):
    while que[0] != arr[i]:
      que.append(que.popleft())
      count += 1
    que.popleft()
  else:
    while que[0] != arr[i]:
      que.appendleft(que.pop())
      count += 1
    que.popleft()
    
print(count)