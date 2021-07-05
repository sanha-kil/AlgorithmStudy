# 프로그래머스 2단계 "구명보트"
# 코딩테스트 고득점 Kit 포함 문제

import heapq

def solution(people, limit):
  answer = 0
  people.sort(reverse = True)
  while people:
    k = people.pop()
    for i in range(len(people)):
      if k + people[i] <= limit:
        people.pop(i)
        break
    answer += 1

  return answer

print(solution([70, 50, 80, 50], 100))