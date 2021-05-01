import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
  command = input()
  n = int(input())
  arr = input()[1:-2].split(',')
  if n == 0:
    que = deque([])
  else:
    que = deque(arr)
  command = command.replace('rr','')
  if que != 'error':
    for a in command:
      try:
        if a == 'r':
          que.reverse()
        if a == 'd':
          que.popleft()
      except:
        que = 'error'
        break
  