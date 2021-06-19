import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
answer=[]

for i in range(n):
  x = int(input())
  heapq.heappush(heap, x)
  print(heap)
  answer.append(heap[(len(heap)-1)//2])
  # print(heap[len(heap)//2])

print(answer)