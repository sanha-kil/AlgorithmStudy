# 야근지수 알고리즘
# n = 퇴근시간까지 남아있는 시간
# works = 남은 일의 작업량
# works의 모든 값의 제곱의 합 = 야근피로도. 야근피로도를 최소로 만들어야 함.

def nightshift(x, y):
    works = x
    n = y
    while y != 0:
        works[works.index(max(works))] -= 1
        n -= 1
        if max(works) == 0:                         #남은 작업량이 0이 될시 루프에서 벗어남(일의 음수화 방지)
            break
    
    answer = 0
    for i in range(0, len(works)):
        answer += works[i] ** 2
    return answer