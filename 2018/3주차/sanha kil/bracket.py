# 올바른 괄호 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/12929?language=python3
# n개의 괄호쌍을 이용해 만들 수 있는 괄호의 종류를 A(n)이라고 할 때,
# A(n-1)의 각 경우의 수에 대해 ()을 앞에 붙이거나, ()를 뒤에 붙이거나, ()로 감싸거나. 세가지 경우로 진행가능 하다.
# ()가 반복되는, ex) ()()()()() 와 같은 경우의 수는 ()가 앞에 붙든 뒤에 붙든 중복되므로 똑같은 경우의 수로 본다.
# A(n) = A(n-1) * 3 - 1
# 위의 점화식 성립
# A(1) = 1

def braket(n):
    answer = 1
    for i in range(1, n):
        answer = answer*3-1
    return answer


# 구글에 검색해보니 카탈랑 수를 이용한 풀이가 있어 가지고 와봤음.
# https://ko.wikipedia.org/wiki/카탈랑_수

def case_number(t):
    n = [1]
    for u in range(2*t+1):  # 2t+1층만큼의 파스칼의 삼각형을 그립니다. (1, 3, 5, 7...)
        m = n[:]  # m은 파스칼의 삼각형의 1줄입니다.
        for v in range(len(m) - 1):
            n[v + 1] += m[v]
        n.append(1)
    return m[t] - m[t-1]  # 파스칼의 삼각형 가운데 값과 그 옆 값의 차입니다.