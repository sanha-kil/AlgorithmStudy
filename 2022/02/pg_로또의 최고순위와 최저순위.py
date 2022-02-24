def solution(lottos, win_nums):
  idx = [6,6,5,4,3,2,1]
  point = 0
  xcount = 0
  for x in lottos:
    if x in win_nums:
      point += 1
    elif x == 0:
      xcount += 1
  print(point, xcount)
  answer = [idx[point+xcount], idx[point]]
  return answer