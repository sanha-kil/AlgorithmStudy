# 프로그래머스 1단계 "메뉴 리뉴얼"

def solution(answers):
  k = len(answers)
  a = [1,2,3,4,5] * ((k//5)+1)
  b = [2,1,2,3,2,4,2,5] * ((k//8)+1)
  c = [3,3,1,1,2,2,4,4,5,5] * ((k//10)+1)
  
  check = [0, 0, 0]

  for i in range(k):
    if answers[i] == a[i]:
      check[0] += 1
    if answers[i] == b[i]:
      check[1] += 1
    if answers[i] == c[i]:
      check[2] += 1
  
  ans = list(i + 1 for i, v in enumerate(check) if v == max(check))
  return ans

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))