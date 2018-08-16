# N-Queen 알고리즘
# n x n 크기의 체스판에서 n개의 퀸이 서로 공격할 수 없는 배치의 경우의 수를 구하는 문제
# 전수조사 경우의 수를 이용하게 되면 n^n의 경우의 수가 발생 -> 매우 비효율적일 것이다.
# 한참을 고민하다가 검색을 통해 백트래킹 방법을 이용해야 된다는 것을 알게됨.
# 경우의 수 중 가능성이 있는 경우의 수를 찾아 마지막 연산 까지 도달하는 방법
# 알고리즘의 동작 자체는 이해하기 매우 쉬웠지만 재귀를 이용해 구현하는게 매우 힘들었음.
# 이틀 잡고 풀었으니 어려움에 주의할 것

def check(m, n):
    result = list()
    if n == 1:
        for i in range(1,m+1):
            result.append([i])
        return result
    elif m < n:
        return []
    else:
        for i in check(m, n-1):
            for j in range(1,m+1):
                if not(j in i) and all([abs(i[k] - j) != (n-1-k) for k in range(n-1)]):
                    result.append(i+[j])
        return result

# solution
def nqueen(n):
    return check(n, n)