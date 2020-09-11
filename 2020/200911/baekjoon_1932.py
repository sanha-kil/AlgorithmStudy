'''
    백준 1932번 정수삼각형 문제
'''

import sys
 
 
n=int(input())
triangle=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=[]
for i in range(1,n+1):
    result.append([0 for _ in range(i)]) #결과 담을곳
 
 
 
for i in range(n):
    if i==0:
        result[0][0]=triangle[0][0]
    else:
        for k in range(i+1):
            if k==0:        #처음 인자의 위층은 하나
                result[i][k]=result[i-1][k]+triangle[i][k]
            elif k==i:      #마지막 인자의 위층은 하나
                result[i][k] = result[i-1][k-1] + triangle[i][k]
            else:
                if result[i-1][k-1]>result[i-1][k]:     #왼쪽대각선 위층이 더 크면
                    result[i][k]=result[i-1][k-1]+triangle[i][k]
                else:                                   #오른쪽대각선 위층이 더크면
                    result[i][k]=result[i-1][k]+triangle[i][k]
 
 
print(max(result[n-1])) #가장아래층까지의 합중에서 가장큰값