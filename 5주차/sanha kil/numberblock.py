# 숫자블록 알고리즘
# 블록의 번호가 n일 때, 처음 블록은 n*2, 두번째 블록은 n*3.... 의 패턴으로 숫자 블록을 배치
# 특정구간의 시작과 끝 번호(begin, end)를 받아 이 특정구간이 어떤 숫자블록으로 이루어져 있는지를 반환


# 소수 구하는 함수
def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else :
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True

def arng(i):
    if i == 1:
        return 0
    elif i % 2 == 0:
        if i/2 > 1000000000:
            return arng(i/2)
        else:
            return int(i/2)
    elif i % 3 == 0:
        if i/3 > 1000000000:
            return arng(i/3)
        else:
            return int(i/3)
    elif is_prime(i) == 1 :
        return 1
    elif i/2 > 1000000000 or i/3 > 1000000000:


# solution
def numblock(begin, end):
    arr = []
    for i in range(begin, end+1):
        arr.append(arng(i))
    return arr

# 아니 문제 푸는 데 프로그래머스 블록 제한 둔게 문제에 적용이 안되있음
# 빨리 풀고 백준 ㄱㄱ;