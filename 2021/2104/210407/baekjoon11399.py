import sys
input = sys.stdin.readline

n = str(input())
arr = list(map(int, input().split()))
arr.sort()

tmp = 0
ans = 0

for i in arr:
  tmp += i
  ans += tmp

print(ans)