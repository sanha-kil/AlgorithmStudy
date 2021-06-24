# 프로그래머스 1단계 "완주하지 못한 선수"

import sys
input = sys.stdin.readline

def solution(participant, completion):
  hashmap = {}
  hashvalue = 0
  for p in participant:
    hashmap[hash(p)] = p
    hashvalue += hash(p)
  
  for c in completion:
    hashvalue -= hash(c)

  return hashmap[hashvalue]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))