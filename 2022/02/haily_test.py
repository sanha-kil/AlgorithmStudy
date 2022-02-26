def solution(tickets, requests):
  result= tickets
  arr = sorted(requests, key = lambda x: (x[0], -x[1]))
  for k in arr:
    if result >= k[1]:
      result -= k[1]

  return tickets-result

# print(solution(10, [[2,3],[1,7],[2,4],[3,5]]))

def rsp_winner(hands):
  if 'R' in hands and 'S' in hands:
    return 'R'
  elif 'R' in hands and 'P' in hands:
    return 'P'
  elif 'P' in hands and 'S' in hands:
    return 'S'

def rsp_loser(hands):
  if 'R' in hands and 'S' in hands:
    return 'S'
  elif 'R' in hands and 'P' in hands:
    return 'R'
  elif 'P' in hands and 'S' in hands:
    return 'P'

def solution2(n, m, points, hands):
  answer_arr = [0 for i in range(n)]
  temp_points = points + [0]

  for i in range(m):
    dict = {}

    for str in hands[i]:
      if str in dict:
        dict[str] += 1
      else:
        dict[str] = 1

    values = dict.values()
    keys = dict.keys()
    key_length = len(keys)

    if key_length == 1:
      temp_points[i+1] += temp_points[i]
    elif key_length == 2:
      target = rsp_winner(keys) if temp_points[i] >= 0 else rsp_loser(keys)
      for j in range(len(hands[i])):
        if hands[i][j] == target:
          answer_arr[j] += temp_points[i] 
    else:
      temp_dict = {}
      for v in values:
        if v in temp_dict:
          temp_dict[v] += 1
        else:
          temp_dict[v] = 1
      
      check = len(temp_dict.keys())

      if check == 1:
        temp_points[i+1] += temp_points[i]
      elif check == 2:
        target=''
        for k, v in dict.items():
          if v == min(temp_dict, key=temp_dict.get):
            target = k
        for j in range(len(hands[i])):
          if hands[i][j] == target:
            answer_arr[j] += temp_points[i] 

      else:
        if temp_points[i] >= 0:
          del dict[max(dict, key=dict.get)]
          temp_keys = temp_dict.keys()
          target = rsp_winner(keys)
          for j in range(len(hands[i])):
            if hands[i][j] == target:
              answer_arr[j] += temp_points[i] 
        else:
          del dict[min(dict, key=dict.get)]
          temp_keys = temp_dict.keys()
          target = rsp_loser(keys)
          for j in range(len(hands[i])):
            if hands[i][j] == target:
              answer_arr[j] += temp_points[i] 

  return max(answer_arr)


print(solution2(7,2,[5,-2], ["PSPPRSS", "SSRRSRP"]))
