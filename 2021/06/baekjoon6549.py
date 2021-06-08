import sys
input = sys.stdin.readline

while 1:
  n, *arr = list(map(int, input().split()))

  if n == 0:
    break

  stack = []
  answer = []

  for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
      idx = stack.pop()
      try:
        answer.append(arr[idx]*(i-stack[-1]-1))
      except:
        answer.append(arr[idx]*i)
    stack.append(i)

  while stack:
    idx = stack.pop()
    try:
      answer.append(arr[idx]*(n-stack[-1]-1))
    except:
      answer.append(arr[idx]*n)

  print(max(answer))