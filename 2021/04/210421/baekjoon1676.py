import sys
from math import factorial
input = sys.stdin.readline

n = factorial(int(input()))
n = str(n)

count = 0
for i in range(len(n)-1, -1, -1):
  if n[i] == '0':
    count += 1
  else:
    break

print(count)

n = int(input())
print(n//5+n//25+n//125)