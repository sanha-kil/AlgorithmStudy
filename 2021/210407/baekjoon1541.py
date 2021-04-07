import sys
input = sys.stdin.readline

arr = input().split('-')
ans = []

for x in arr:
  tmp = x.split('+')
  num = 0
  for y in tmp:
    num += int(y)
  ans.append(num)

for i in range(1, len(ans)):
  ans[0] -= ans[i]

print(ans[0])