import sys
inpout = sys.stdin.readline

while 1:
  s = input()

  if s == '.':
    break

  stack = []
  check = True
  for i in range(len(s)):
    if s[i] == '(' or s[i] == '[':
      stack.append(s[i])
    elif s[i] == ')':
      if not stack or stack[-1] == '[':
        check = False
        break
      elif stack[-1] == '(':
        stack.pop()
        continue
    elif s[i] == ']':
      if not stack or stack[-1] == '(':
        check = False
        break
      elif stack[-1] == '[':
        stack.pop()
        continue

  if not stack and check == True:
    print('yes')
  else:
    print('no')