import sys
input = sys.stdin.readline

for _ in range(int(input())):
  count = 0
  s = input()
  for i in range(len(s)-1):
    if s[i] == '(':
      count += 1
    else:
      if count == 0:
        count = -1
        break
      else:
        count -= 1
  
  if count == 0:
    print('YES')
  else:
    print('NO')

