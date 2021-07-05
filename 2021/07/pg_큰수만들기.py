# 프로그래머스 2단계 "큰 수 만들기"
# 코딩테스트 고득점 Kit 포함 문제

def solution(number, k):
  num = str(number)
  count = 0
  # 문자열 스택
  answer = ''
  for x in num:
    # 인접한 수가 현재 들어가는 수보다 작을 경우 인접한 수 제거
    while answer and count < k and answer[-1] < x:
      answer = answer[:-1]
      # 여태 얼마나 빼주었는지 확인하기 위해 count += 1
      count += 1

    # 숫자 추가
    answer += x
  
  # k값 만큼 빼주지 못했을 경우 더 빼주어야 하는 만큼 뒷자리 제거
  return answer if count == k else answer[:-(k-count)]

print(solution("1924", 2))