# 프로그래머스 2단계 "프린터"
# 코딩테스트 고득점 Kit 포함

from collections import deque

def solution(priorities, location):
  deq = deque(priorities)
  idx = deque([i for i in range(len(priorities))])
  answer = []
  while deq:
    if deq[0] == max(deq):
      deq.popleft()
      answer.append(idx.popleft())
    else:
      deq.append(deq.popleft())
      idx.append(idx.popleft())
  
  return answer.index(location)+1

solution([2, 1, 3, 2],2)