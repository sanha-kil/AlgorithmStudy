# 프로그래머스 2단계 "주식가격"
# 코딩테스트 고득점 Kit 포함 문제

def solution(prices):
  stack = []
  answer = [0 for _ in range(len(prices))]
  for i in range(len(prices)):
    # 스택에 담겨있는 인덱스를 이용하여 price[i]보다 높은 가격의 시점을 빼줌
    while stack and prices[stack[-1]] > prices[i]: 
      # 1초뒤에 가격이 떨어지므로 pop 해줄 때 +1을 해준다
      answer[stack.pop()] += 1

    # 스택에 담겨있는 시점들에 1초씩 더해준다
    for j in range(len(stack)):
      answer[stack[j]] += 1
    
    # 새로운 시점 추가
    stack.append(i)
  return answer

print(solution([1, 2, 3, 2, 3]))