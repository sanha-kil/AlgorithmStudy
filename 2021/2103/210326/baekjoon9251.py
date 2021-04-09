import sys

input = sys.stdin.readline

a = ' '+str(input().rstrip())
b = ' '+str(input().rstrip())
lcs = [[0]*len(a) for i in range(len(b))]

for i in range(1, len(b)):
  for j in range(1, len(a)):
    if b[i] == a[j]:
      lcs[i][j] = lcs[i-1][j-1]+1
    else:
      lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[len(b)-1][len(a)-1])