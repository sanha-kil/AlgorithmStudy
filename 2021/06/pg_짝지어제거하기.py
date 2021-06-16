# 프로그래머스 2단께 짝지어 제거하기
# 2017 팁스타운 출제
# 스택 사용 문제

def solution(s):
  stack = []
  for x in s:
    stack.append(x)
    try:
      if stack[-1] == stack[-2]:
        stack.pop()
        stack.pop() 
    except:
      continue
  if stack:
    return 0
  else:
    return 1

print(solution('cdcd'))