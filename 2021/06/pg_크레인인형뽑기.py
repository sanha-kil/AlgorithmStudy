def solution(board, moves):
    n = len(board)
    b_list = board
    stack = []
    answer = 0

    for a in moves:
      for i in range(n):
        if b_list[i][a-1] != 0:
          stack.append(b_list[i][a-1])
          b_list[i][a-1] = 0
          break
      
      try:
        if stack[-1] == stack[-2]:
          stack.pop()
          stack.pop()
          answer += 2
      except:
        continue
      
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))