import sys
from math import factorial
input = sys.stdin.readline

num = int(input())
for _ in range(num):
  n, m = map(int,input().split())
  print(factorial(m)//(factorial(n)*factorial(m-n)))