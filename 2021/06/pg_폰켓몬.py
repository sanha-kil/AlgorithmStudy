# 프로그래머스 1단계 "폰켓몬"
# 찾아라 프로그래밍 마에스트로 출제 문제

import sys
input = sys.stdin.readline

def solution(nums):
  a = len(set(nums))

  if len(nums)//2 > a:
    return a
  else:
    return len(nums)//2

print(solution([3,1,2,3]))