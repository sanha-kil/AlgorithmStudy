import sys
input = sys.stdin.readline

def cut(p, n):
  global blue, white
  check = p[0][0]
  ex = False

  for i in range(n):
    if ex:
      break

    for j in range(n):
      if p[i][j] != check:
        cut([row[:n//2] for row in p[:n//2]], n//2)
        cut([row[n//2:n] for row in p[:n//2]], n//2)
        cut([row[:n//2] for row in p[n//2:n]], n//2)
        cut([row[n//2:n] for row in p[n//2:n]], n//2)
        ex = True
        break
    
  if not ex:
    if check == 1:
      blue += 1
    else:
      white += 1

n = int(input())
paper = []
white = 0
blue = 0
for _ in range(n):
  paper.append(list(map(int, input().split())))

cut(paper, n)

print(white)
print(blue)