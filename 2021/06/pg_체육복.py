def solution(n, lost, reserve):
  lost1 = set(lost)- set(reserve)
  reserve1 = set(reserve) - set(lost)

  for a in reserve1:
    if a-1 in lost1:
      lost1.remove(a-1)
    elif a+1 in lost1:
      lost1.remove(a+1)

  return n-len(lost1)
