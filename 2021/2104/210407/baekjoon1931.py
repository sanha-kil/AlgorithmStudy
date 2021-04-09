import sys
input = sys.stdin.readline

n = int(input())
arr = []
answer = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1],x[0]))

count = 1
tmp = arr[0][1]
for i in range(1, n):
    if tmp <= arr[i][0]:
      count += 1
      tmp = arr[i][1]

print(count)