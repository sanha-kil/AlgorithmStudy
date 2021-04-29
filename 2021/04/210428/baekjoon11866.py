import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
que = deque([i for i in range(1, n+1)])
answer = []

while len(que) > 0:
  for _ in range(k-1):
    que.append(que.popleft())
  answer.append(que.popleft())

print('<', end="")
print(*answer, sep=', ', end='>\n')