# 최소값 알고리즘
# 두 배열의 수들을 각각 서로 곱해 그 합들이 최소값이여야 함
# 
a = [1,2,3,4]
print(a.pop(a.index(max(a))))

def solution(A,B):
    k = 0
    s = len(A)
    for i in range(0, s):
        k += (A.pop(A.index(max(A))) * B.pop(B.index(min(B))))
    answer = k
    return answer