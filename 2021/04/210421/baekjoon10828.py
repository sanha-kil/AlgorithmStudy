import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
  s = input().split()
  if s[0] == 'push':
    stack.append(int(s[1]))
  if s[0] == 'pop':
    if not stack:
      print(-1)
    else:
      print(stack.pop(len(stack)-1))
  if s[0] == 'size':
    print(len(stack))
  if s[0] == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  if s[0] == 'top':
    if not stack:
      print(-1)
    else:
      print(stack[len(stack)-1])