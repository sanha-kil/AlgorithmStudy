# N개의 최소공배수 알고리즘
# 유클리드 호제법을 이용하여 최소공배수 구하도록 함
# 람다와 reduce 함수를 이용하여 코드의 단축화를 시도해 보았음
# https://wikidocs.net/64 참고

from functools import reduce

def nlcm(num):

    # 최대공약수 구하기: 유클리드 호제법 적용
    def get_gcd(x, y):
        while y:
          x, y = y, x%y
        return x

    answer = reduce(lambda x, y: (x*y)//get_gcd(x, y), num)
    return answer

    # 파이썬에서의 람다 : lambda 인자 : 표현식 
    # reduce() : 배열을 받아 특정 함수를 배열에 대해 누적실행