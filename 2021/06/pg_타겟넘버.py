import sys
input = sys.stdin.readline

def dfs(n, numbers, target):
  x = n + numbers[0]
  y = n - numbers[0]
  if len(numbers) == 1:
    if target == x or target == y:
      return 1
    else:
      return 0
  
  return dfs(x, numbers[1:], target) + dfs(y, numbers[1:], target)

def solution(numbers, target):
  answer = dfs(numbers[0], numbers[1:], target) + dfs(-numbers[0], numbers[1:], target)
  return answer

print(solution([1, 1, 1, 1, 1], 3))