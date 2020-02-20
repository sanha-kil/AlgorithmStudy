# 최고의 집합 알고리즘
# 자연수 n개로 이루어진 집합 중에 1. 각 원소의 합이 S가 되는 수의 집합
#                          2. 위 조건을 만족하면서 각 원소의 곱이 최대가 되는 집합
# 을 성립하는 집합을 최고의 집합이라고 한다.
# 집합의 원소 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 리턴하는 함수 설계

def best(n, s):
    if n > s:
        return [-1]                     # n > s 일 때 집합성립X
    
    else:
        answer = [s//n] * n
        for i in range(0, s%n):
            answer[n-i-1] += 1
        return answer


