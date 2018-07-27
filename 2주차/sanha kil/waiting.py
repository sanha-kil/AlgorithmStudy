# 줄 서는 방법 알고리즘
# 팩토리얼을 이용하여 문제해결
# 줄 서는 방법은 n!개이며 i번째 자리마다 (n-i)!개의 경우의 수 존재
# k//(n-i)! 를 이용하여 각 자리의 인덱스를 구해 배열에 넣고 k%(n-i)!을 다음 연산에 사용. 이를 반복

def waiting(n, k):

    def fac(f):                                     # 팩토리얼 함수. 소스를 가지고 올 수 있지만 걍 만들어봄
        a = 1
        for j in range(1, f+1):
            a *= j
        return a
    
    answer = []
    wlist = [i for i in range(1, n+1)]              # [1, 2, ... , n] 배열 생성
    k -= 1                                          # wlist[i]가 i-1 이므로 인덱스의 올바른 작동을 위하여 k-1 실행 
    
    for i in range(1, n):
        answer.append(wlist.pop(k//fac(n-i)))       
        k %= fac(n-i)                               # 다음 연산을 위해 k를 나머지로 변경함
        if len(wlist) == 1:                         # wlist에 남은 항목이 하나밖에 없을 때 마저 answer에 넣고 반복 종료
            answer.append(wlist.pop())
            break
    return answer