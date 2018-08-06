# 124 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3
# 자연수 n을 3으로 나눠 나머지가 1이면 1, 2이면 2, 0 이면 4를 출력 (뒷자리부터)

def otf(n):
    array = []
    while n > 0:
        if n % 3 == 1:
            array.append(0, '1')
        elif n % 3 == 2:
            array.append(0, '2')
        elif n % 3 == 0:
            array.append(0, '4')
            n -= 1
        n = n // 3
    
    answer = ''
    if i in range(0, len(array)):
        answer += array[i]
    
    return answer