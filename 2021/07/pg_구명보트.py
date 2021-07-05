# 프로그래머스 2단계 "구명보트"
# 코딩테스트 고득점 Kit 포함 문제

def solution(people, limit):
  answer = 0
  people.sort()
  i, j = 0, len(people)-1
  while i <= j:
    if people[i] + people[j] <= limit:
      i += 1
    j-=1
    answer += 1

  return answer

print(solution([70, 50, 80, 50], 100))