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
        print('(', end='')
        quad_tree([row[:n//2] for row in p[:n//2]], n//2)
        quad_tree([row[n//2:n] for row in p[:n//2]], n//2)
        quad_tree([row[:n//2] for row in p[n//2:n]], n//2)
        quad_tree([row[n//2:n] for row in p[n//2:n]], n//2)
        ex = True
        print(')', end='')
        break
    
  if not ex:
    print(check, end='')

n = int(input())
paper = []
for i in range(n):
  paper.append(input().strip())

quad_tree(paper, n)