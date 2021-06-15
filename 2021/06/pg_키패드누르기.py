import sys
input = sys.stdin.readline

def solution(numbers, hand):
  crt = {'left':10, 'right':12}
  answer = ''
  for k in numbers:
    if k == 0:
      k = 11
    if k == 1 or k == 4 or k == 7:
      answer += 'L'
      crt['left'] = k
    elif k == 3 or k == 6 or k == 9:
      answer += 'R'
      crt['right'] = k
    else:
      left_dis = abs(k-crt['left'])//3 + abs(k-crt['left'])%3
      right_dis = abs(k-crt['right'])//3 + abs(k-crt['right'])%3
      if left_dis > right_dis:
        answer += 'R'
        crt['right'] = k
      elif left_dis < right_dis:
        answer += 'L'
        crt['left'] = k
      else:
        if hand == 'left':
          answer += 'L'
          crt['left'] = k
        else:
          answer += 'R'
          crt['right'] = k
  
  return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))