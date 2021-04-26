import sys
input = sys.stdin.readline

n = int(input())

s = []
for i in range(n):
  s.append(int(input()))

stack = []
answer = []
count = 0

for i in range(1, n+1):
  stack.append(i)
  answer.append('+')
  while stack[-1] == s[count]:
    stack.pop()
    answer.append('-')
    count += 1
    if not stack:
      break

if not stack:
  for i in range(len(answer)):
    print(answer[i])
else:
  print('NO')