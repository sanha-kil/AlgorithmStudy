import sys

# 백준 2580번 문제
# 백트래킹을 이용한 스도쿠 문제 풀이

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = []
end = False

def checkZero():                            # 0(문제에서의 빈칸)의 위치를 찾기 위함 함수
    for i in range(9):
        for j in range(9):
            if 0 == arr[i][j]:
                zero.append((i, j))

def checkNum(x, y):                         # 해당 좌표에 들어갈수 있는 수를 검사하는 함수
    global arr
    num = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if arr[x][i] in num:
            num.remove(arr[x][i])
        if arr[i][y] in num:
            num.remove(arr[i][y])
    if len(num) > 0:
        for i in range((x//3)*3, ((x//3)*3)+3):
            for j in range((y//3)*3, ((y//3)*3)+3):
                if arr[i][j] in num:
                    num.remove(arr[i][j])
    return num

def dfs(n):
    global end
    if n == len(zero):
        end = True                      # 해당 케이스가 정답일시 배열을 유지하기 위해 불린타입 end를 True로
        return
    
    x, y = zero[n]
    for k in checkNum(x, y):
        arr[x][y] = k
        dfs(n+1)
        if end:
            return
    
    if end == False:                    # 해당 케이스가 정답이 아닐시 배열을 원상태로
        arr[x][y] = 0

checkZero()
dfs(0)
for i in range(9):
    print(*arr[i])
