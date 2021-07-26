# 프로그래머스 3단계 "섬 연결하기"
# 코딩테스트 고득점 Kit 포함 문제

def solution(n, costs):
  answer = 0
  # 비용을 기준으로 정렬
  costs.sort(key = lambda x: x[2])
  # set 자료형 선언
  check = set([costs[0][0]])

  while len(check) < n:
    # 비용이 적은 간선부터 추가
    # 사이클이 형성되는지 확인. 사이클이 형성되는 간선의 경우 넘어감
    for x in costs:
      if x[0] in check and x[1] in check:
        continue
      elif x[0] in check or x[1] in check:
        answer += x[2]
        check.update([x[0], x[1]])
        costs.pop(costs.index(x))
        break

  return answer