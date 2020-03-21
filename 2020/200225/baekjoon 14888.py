import sys

# 백준 14888번 연산자 끼워넣기 문제
# 백트래킹, 재귀를 이용하여 주어진 연산자를 순서대로 계산
# 그 중 최댓값과 최솟값을 출력

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operlist = list(map(int, sys.stdin.readline().split()))
reslist = []

def operation(n, res, ops):
    if n == len(num):                               # 주어진 연산자를 다 사용했을 경우 결과값을 배열에 추가
        reslist.append(res)
        return

    if ops[0] > 0:                                  # 연산자 4개의 경우의 수를 나눠 재귀
        ops[0] -= 1
        operation(n+1, res+num[n], ops)
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        operation(n+1, res-num[n], ops)
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        operation(n+1, res*num[n], ops)
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        operation(n+1, int(res/num[n]), ops)
        ops[3] += 1

operation(1, num[0], operlist)
print(max(reslist))
print(min(reslist))                                 # 결과값이 모여있는 배열에서 최댓값과 최솟값을 출력