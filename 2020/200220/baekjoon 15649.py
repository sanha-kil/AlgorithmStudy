import sys
import math

#백준 15649 'N과 M(1)'
#백트래킹, 깊이 우선 탐색 알고리즘 사용

n, m = map(int, input().split()) # N, M 받기
num = [i for i in range(n+1)]    # 1부터 N까지 숫자 리스트 선언
check = [False]*(n+1)            # 1부터 N까지 탐색을 위한 불타입 리스트 선언

tmp = []

def bktr(x):
    if x == m:                   # 탐색의 길이가 M까지 도달하면 진행 중인 탐색을 중단
        print(*tmp)              # 탐색된 수열 출력
        return                   
    
    for i in range(1, n+1):      # 1부터 N까지 수열 생성
        if check[i]==True:       # 이미 수열에 사용된 수일시 건너 뜀
            continue

        check[i] = True
        tmp.append(num[i])       
        bktr(x+1)                # 현재 숫자가 수열에 중복되지 않았을 시 수열에 넣고 자식노드 탐색
        
        tmp.pop()
        check[i] = False         # 자식 노드에 대한 탐색 종료 후 탐색중인 수열에서 해당 숫자 POP

bktr(0)