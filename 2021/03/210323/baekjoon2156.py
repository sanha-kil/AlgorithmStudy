import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
dp=[arr[0]]
if(n>1):
  dp.append(arr[0]+arr[1])

for i in range(2, n):
  if i == 2:
    dp.append(max(arr[i]+dp[i-2], arr[i]+arr[i-1], dp[i-1]))
  else:
    dp.append(max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1]))

print(dp[n-1])