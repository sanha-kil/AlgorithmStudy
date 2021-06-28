# 프로그래머스 2단계 "위장"
# 프로그래머스 코딩테스트 고득정 Kit 포함 문제

def solution(clothes):
  dict = {}  # 각 옷 종류마다 보유 개수
  for x in clothes:
    if x[1] not in dict:
      dict[x[1]] = 1
    else:
      dict[x[1]] += 1
  
  li = list(dict.values())
  answer = 1
  for i in li:
    answer *= (i + 1) # 해당 옷 종류를 안입는 경우 추가

  return answer - 1 # 다 벗은 경우 제외

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))