# 프로그래머스 Level3 '정수 삼각형'
# 코딩테스트 고득점 Kit 포함 문제

def solution(triangle):
  for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
      if j == 0:
        triangle[i][j] += triangle[i-1][j]
      elif i == j:
        triangle[i][j] += triangle[i-1][j-1]
      else:
        triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
  answer = max(triangle[-1])
  return answer