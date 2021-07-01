# 프로그래머스 3단계 "이중우선순위 큐"
# 코딩테스트 고득점 Kit 포함 문제

import heapq

def solution(operations):
  que = []

  for x in operations:
    oper, num = x.split()
    num = int(num)

    # 인덱스 오류날 시를 대비한 예외 처리
    try:
      if x == 'D 1':
        # heapq의 nlargest를 이용하여 최대값을 구하고, 해당 인덱스 pop
        print(heapq.nlargest(1, que)[0])
        que.pop(que.index(heapq.nlargest(1, que)[0]))
      elif x == 'D -1':
        # heappop을 이용해 최소값 pop
        heapq.heappop(que)
      else:
        # I일 경우 이중순위큐에 push
        heapq.heappush(que, num)
    except IndexError:
      pass

  if not que:
    return [0, 0]
  else:
    return [max(que), min(que)]

print(solution(["I 16","D 1"]))