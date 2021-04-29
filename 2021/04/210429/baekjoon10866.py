import sys
from collections import deque
input = sys.stdin.readline

que = deque([])
for _ in range(int(input())):
  s = input().split()
  if s[0] == 'push_back':
    que.append(s[1])
  elif s[0] == 'push_front':
    que.appendleft(s[1])
  elif s[0] == 'pop_front':
    if que:
      print(que.popleft())
    else:
      print(-1)
  elif s[0] == 'pop_back':
    if que:
      print(que.pop())
    else:
      print(-1)
  elif s[0] == 'size':
    print(len(que))
  elif s[0] == 'empty':
    if que:
      print(0)
    else:
      print(1)
  elif s[0] == 'front':
    if que:
      print(que[0])
    else:
      print(-1)
  elif s[0] == 'back':
    if que:
      print(que[-1])
    else:
      print(-1)