import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

#Max Heap
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)