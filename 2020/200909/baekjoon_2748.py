# baekjoon 2748번 분제 피보나치 수열

def dy_fib(n):
    flist = [0, 1]
    if n < 2:
        return flist[n]
    else:
        for i in range(2, n+1):
            flist.append(flist[i-1] + flist[i-2])
        return flist[n]

x = int(input())
print(dy_fib(x))

# 다이나믹 프로그래밍을 이용한 피보나치 수열
