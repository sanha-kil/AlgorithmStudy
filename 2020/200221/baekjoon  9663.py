import sys
import math

# 백준 9663번 문제
# N-Queen : N*N 체스판 위 N개의 퀸이 서로를 공격학 수 없도록 배치하는 경우의 수 탐색
# 백트래킹 사용
# 문제 자체는 정답이나 파이썬 특성상 시간 초과로 오답

n = int(input())
count = 0
arr = []

def check(x):                                                       # x행의 y좌표와 1부터 x-1행의 y좌표를 직선, 대각선 비교
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
            return False
    return True                                                     # 해당이 안될시 True 반환

def nq(x):
    global count
    if x == n:
        count += 1
    
    else:
        for i in range(n):
            arr.append(i)
            if check(x) == True:                                    # 부모노드들과 직선, 대각선체크를 마친후 이상 없으면 자식노드로 탐색 진행
                nq(x+1)
            arr.pop()


nq(0)
print(count)