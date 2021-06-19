import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0

while n>1:
  answer += n%k + 1
  n //= k

print(answer)