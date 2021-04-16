import sys
input = sys.stdin.readline

for _ in range(int(input())):
  dress = dict()
  n = int(input())
  if n == 0:
    print(0)
    continue

  for _ in range(n):
    name, type = map(str, input().split())
    if type in dress.keys():
      dress[type] += 1
    else:
      dress[type] = 1
    
    ans = 1
    for tmp in dress.keys():
      ans *= dress[tmp] + 1
    ans -= 1
  print(ans)
