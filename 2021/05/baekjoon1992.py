import sys
input = sys.stdin.readline

def quad_tree(p, n):
  check = p[0][0]
  ex = False

  for i in range(n):
    if ex:
      break

    for j in range(n):
      if p[i][j] != check:
        quad_tree([row[:n//2] for row in p[:n//2]], n//2)
        quad_tree([row[n//2:n] for row in p[:n//2]], n//2)
        quad_tree([row[:n//2] for row in p[n//2:n]], n//2)
        quad_tree([row[n//2:n] for row in p[n//2:n]], n//2)
        ex = True
        break
    
  if not ex:
    if check == 1:
      blue += 1
    else:
      white += 1

n = int(input())
paper = []
for i in range(n):
  paper.append(input().strip().split())
  print(paper[i])