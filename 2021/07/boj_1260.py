# 백준 1260번 'DFS와 BFS'
# DFS, BFS
# 블로그 작성 예정

def dfs(v):
    print(v, end=' ')
    check[v] = 1
    for i in range(1, n + 1):
        if check[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    check[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if check[i] == 1 and s[v][i] == 1:
                queue.append(i)
                check[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
check = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1