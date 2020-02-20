# 2*N 타일링 알고리즘
# 2*1 타일을 세로로 넣거나 가로로 두개를 넣는 두가지 방법이 존재하게 된다.
# [n-1의 경우의 수 + 2*1 세로 타일] + [n-2의 경우의 수 + 2*1 가로 타일 2개]로 알고리즘 구현가능
# 이는 피보나치 수열과 같다.

def twoxn(n):
    count = [0, 1, 2]
    if n < 3:
        return count[n]
    for i in range(3, n+1):
        count.append((count[i-1] + count[i-2]) % 1000000007)
    answer = count[n] % 1000000007
    return answer