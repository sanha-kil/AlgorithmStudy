import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

tmp = price[0]
ans = 0

for i in range(n-1):
  if(price[i] < tmp):
    tmp = price[i]
  ans += tmp * distance[i]

print(ans)