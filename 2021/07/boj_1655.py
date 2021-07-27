# 백준 1655번 '가운데를 말해요'
# 우선순위 큐

import heapq
import sys
input = sys.stdin.readline

maxQ, minQ = [], []

N = int(input())
for i in range(N):
    now = int(input())
    if i % 2 == 0:
        heapq.heappush(maxQ, now*-1)
    else:
        heapq.heappush(minQ, now)
    if maxQ and minQ and maxQ[0]*-1 > minQ[0]:
        temp = heapq.heappop(maxQ)*-1
        heapq.heappush(maxQ, heapq.heappop(minQ)*-1)
        heapq.heappush(minQ, temp)
    print(maxQ[0]*-1)