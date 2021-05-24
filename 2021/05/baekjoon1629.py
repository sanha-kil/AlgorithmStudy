import sys
input = sys.stdin.readline

def solve(power):
  if power == 1:
    return a%c

  if power%2 == 0:
    return solve(power//2)**2 % c
  else:
    return solve(power//2)**2 * a % c

a, b, c = map(int, input().split())

print(solve(b))