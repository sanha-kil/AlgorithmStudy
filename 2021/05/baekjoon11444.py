import sys
input = sys.stdin.readline

def fibo(n):
    sq5 = 5**(0.5)
    answer = 1/sq5*(((1+sq5)/2)**n - ((1-sq5)/2)**n)
    return int(answer)

n = int(input())

print(fibo(n))

