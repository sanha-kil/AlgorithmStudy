import sys
input = sys.stdin.readline

n = int(input())

def gcd(a, b):
  x, y = a, b
  while y > 0:
    x %= y
    x, y = y, x
  return x

for _ in range(n):
  a, b = map(int, input().split())
  num = gcd(a, b)
  print(a*b//num)