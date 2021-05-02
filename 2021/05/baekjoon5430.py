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
  command = command.replace('RR','')
  
  check = True
  isReversed = False
  
  for a in command:
    try:
      if a == 'R':
        isReversed = not isReversed
      if a == 'D':
        if isReversed == False:
          que.popleft()
        else:
          que.pop()
    except:
      check = False
      break

  if isReversed == True:
    que.reverse()

  if check == False:
    print('error')
  else:
    print('['+ ','.join(que) +']')