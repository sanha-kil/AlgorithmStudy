'''
    백준 1904번 01타일문제. 
    자릿수 N 내에서 00과 1 타일을 배치하는 경우의 수를 구하는 문제
    규칙을 차례로 찾다보면 피보나치 수열임을 알 수 있음
'''

def tiling(x):
    tlist = [0] * 1000001
    tlist[1], tlist[2] = 1, 2
    if x > 2:
        for i in range(3, x+1):
            tlist[i] = (tlist[i-1]+tlist[i-2])%15746 # 값들이 int 범위를 넘어가기 때문에 나머지값을 바로 계산해 주어야 함
    return tlist[x]


x = int(input())
print(tiling(x))