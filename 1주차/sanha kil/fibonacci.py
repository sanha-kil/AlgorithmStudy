# 멀리뛰기 알고리즘
# n = 1 일 때 1, n = 2 일 때 2, n = 3 일 때 3, n = 4 일 때 5 ...
# 피보나치 수열을 이용하여 구현
# answer = (n-2)+(n-1)
# 재귀 이용 시 O(n^2), 반복 이용 시 O(n)

def fibonacci_loop(x):              #반복
    a = [1, 2]
    i = 0
    for _ in range(x):
        a.append(a[i] + a[i+1])
        i += 1
    answer = a[x-1]
    return answer

def fibonacci_recursion(x):         #재귀
    if x == 1:
        return 1
    elif x == 2:
        return 2
    answer = fibonacci_recursion(x-2) + fibonacci_recursion(x-1)
    return answer

k = int(input('값을 입력해주세요 : '))
print(fibonacci_loop(k))
print(fibonacci_recursion(k))