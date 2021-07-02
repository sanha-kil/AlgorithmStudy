# 프로그래머스 2단계 "H-Index"
# 코딩테스트 고득점 Kit 포함 문제

def solution(citations):
  citations.sort()
  n = len(citations)
  answer = []

  # 반복문 돌려가며 부합되는 h값 찾기
  for i in range(n):
    # n-i = 해당 논문보다 많거나 같은 수로 인용된 논문의 수
    if citations[i] >= n-i:
      answer.append(n-i)

  # h값 중 최대값 반환
  # answer 배열 비어있을 시 부합되는 h값 없으므로 0 반환
  return max(answer) if answer else 0

print(solution([1,18,19,20]))