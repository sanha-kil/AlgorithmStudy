# 프로그래머스 2단계 "기능개발"

def solution(progresses, speeds):
    que = []
    for i in range(len(progresses)):
        k = 100-progresses[i]
        if (k%speeds[i]) == 0:
            que.append(k//speeds[i])
        else:
            que.append((k//speeds[i])+1)
    print(que)

    answer = []
    check = 0
    for x in que:
        if not answer:
            check = x
            answer.append(1)
            continue
        
        if x > check:
            check = x
            answer.append(1)
        else:
            answer[-1] += 1

    print(answer)
    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])