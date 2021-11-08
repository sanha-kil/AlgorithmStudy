# 프로그래머스 Level2 '등굣길'
# 코딩테스트 고득점 Kit 포함 문제

from itertools import permutations

def primeCheck(n):
  # 에스트라테네스의 채를 이용한 소수 리스트를 반환하는 함수
  checklist = [False,False] + [True]*(n-1)
  primes=[]

  for i in range(2,n+1):
    if checklist[i]:
      primes.append(i)
      for j in range(i*2, n+1, i):
          checklist[j] = False

  return primes

def solution(numbers):
  # itertools의 순열 메소드를 이용한 경우의 수 저장
  sets = []
  for i in range(1, len(numbers)+1):
    sets += list(permutations(list(numbers), i))

  # 문자열 이어 붙인 뒤 숫자로 자료형을 바꾸고 
  # set을 이용해 다시 한번 중복 제거 ('011'이 숫자형 11로 바뀌면서 생기는 중복 제거)
  numlist = []
  for x in sets:
    temp = ''
    for y in x:
      temp += y
    numlist.append(temp)

  numlist = list(set(list(map(int, numlist))))

  # 소수인지 확인
  primetable = primeCheck(max(numlist))
  answer = 0
  for k in numlist:
    if k in primetable:
      answer += 1

  return answer


print(solution('17'))
print(solution('011'))