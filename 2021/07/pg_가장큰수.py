# 프로그래머스 2단계 '가장 큰 수'
# 코딩테스트 고득점 Kit 포함 문제

def solution(numbers):
  numbers = list(map(str, numbers))
  # 람다를 이용하여 x(0이상 1000이하)
  # 큰 값부터 찾기 위해서 reverse = True
  answer = sorted(numbers, key=lambda x: x*3, reverse = True)

  # 구성요소가 모두 0으로 이루어져 있을 경우 한자리 수 0으로 반환하기 위해 int로 변환 후, 다시 str로 변환
  return str(int(''.join(answer)))