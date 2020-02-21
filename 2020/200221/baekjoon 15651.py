import sys
import math

# 백준 15651 'N과 M(3)'
# 백트래킹, 깊이 우선 탐색 알고리즘 사용
# 15649문제와 수열 내 숫자의 중복이 가능

n, m = map(int, input().split()) # N, M 받기
num = [i for i in range(n+1)]    # 1부터 N까지 숫자 리스트 선언

tmp = []

def bktr(x):
    if x == m:                   # 탐색의 길이가 M까지 도달하면 진행 중인 탐색을 중단
        print(*tmp)              # 탐색된 수열 출력
        return                   
    
    for i in range(1, n+1):      # 1부터 N까지 수열 생성
        
        tmp.append(num[i])       
        bktr(x+1)                # 현재 숫자를 수열에 넣고 자식노드 탐색
        
        tmp.pop()

bktr(0) 