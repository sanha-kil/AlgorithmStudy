# 프로그래머스 2단계 더 맵게

import heapq

def solution(scoville, k):
  heap = []
  for x in scoville:
    heapq.heappush(heap, x)

  answer = 0
  while heap[0] < k:
    try:
      heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
      answer+=1
    except:
      return -1
    
  return answer