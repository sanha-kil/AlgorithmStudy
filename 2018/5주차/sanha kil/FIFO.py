# 선입선출 스케줄링 알고리즘
# 작업의 개수 n과 각 코어의 연산속도 cores를 받음
# 각 코어는 작업을 선입선출로 처리함
# 마지막으로 작업을 처리하는 코어를 반환해주면 됨

# 효율성 테스트에서 탈락. 근데 검색해보니 나만 그런게 아닌거 같더라
def fifo(n, cores):
    count = 0
    while n > 0:
        for i in range(0, len(cores)):
            if time%cores[i] == 0:
                n -= 1
                if n == 0:
                    return i+1
        count += 1