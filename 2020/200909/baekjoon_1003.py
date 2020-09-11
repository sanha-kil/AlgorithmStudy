# baekjoon 1003번 분제 피보나치 수열 진행에서 0과 1의 출력

def fibcount(n):
    flist = [0, 1]
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        for i in range(2, n+1):
            flist.append(flist[i-1] + flist[i-2])
        print(flist[n-1], flist[n])

x = int(input())
for _ in range(x):
    fibcount(int(input()))

# 다이나믹 프로그래밍을 이용한 피보나치 수열
