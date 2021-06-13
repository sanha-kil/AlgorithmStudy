# 백준 1654번 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]
left, right = 1, max(line)

while left <= right:
    mid = (left + right) // 2
    tmp = 0

    for i in line:
        tmp += i // mid
        
    if tmp >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)