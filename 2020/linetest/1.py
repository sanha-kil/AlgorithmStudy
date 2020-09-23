def solution(boxes):
    x = []
    for i in range(len(boxes)):
        x = x + boxes[i]
    tmp = sorted(list(set(x)))
    print(tmp)
    answer = 0
    for i in range(len(tmp)):
        if x.count(tmp[i]) % 2 == 1:
            answer = answer + 1
    answer = int(answer / 2)
    return answer

print(solution([[1, 2], [2, 3], [3, 1]]))