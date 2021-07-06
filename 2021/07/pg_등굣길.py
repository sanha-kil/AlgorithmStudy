# 프로그래머스 Level3 '등굣길'
# 코딩테스트 고득점 Kit 포함 문제

def solution(m, n, puddles):
  dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
  dp[1][1] = 1
  for i in range(1, n+1):
    for j in range(1, m+1):
      if dp[i][j] == 1:
        continue
      elif [j, i] in puddles:
        dp[i][j] = 0
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
  return dp[n][m]%1000000007

print(solution(4,3,[[2,2]]))