# 최소값 알고리즘
# 두 배열의 수들을 각각 서로 곱해 그 합들이 최소값이여야 함
# 
def minimum(A,B):
    answer = 0
    while A:
        answer += (A.pop(A.index(max(A))) * B.pop(B.index(min(B))))
    return answer

#혹시 더 좋은 풀이가 있을까 싶어서 검색했는데 나온 람다를 이용한 풀이
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])