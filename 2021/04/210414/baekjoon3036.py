import sys
import fractions
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
  tmp = fractions.Fraction(arr[0], arr[i])
  print(f'{tmp.numerator}/{tmp.denominator}')