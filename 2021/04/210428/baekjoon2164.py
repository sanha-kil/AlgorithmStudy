import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque([i for i in range(1, n+1)])

print(que)
