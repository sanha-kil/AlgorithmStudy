# 프로그래머스 2단계 멀쩡한 사각형

import sys
from math import gcd
input = sys.stdin.readline

def solution(w,h):
  k = gcd(w, h)
  return w*h-((w//k)+(h//k)-1)*k

print(solution(8,12))