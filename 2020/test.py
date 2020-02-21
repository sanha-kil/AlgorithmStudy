def adjacent(x):
    for j in range(x):
        if row[x] == row[j] or abs(row[x] - row[j]) == x - j:
            return 
    return True
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            for j in range(x )
            if adjacent(x):
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)