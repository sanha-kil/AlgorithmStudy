def solution(s):
  dict = {}
  answer = 0
  for str in s:
    if str in dict:
      dict[str] += 1
    else:
      dict[str] = 1

  for i in dict.values():
    if (i%2) == 1:
      answer += 1

  return answer

# print(solution('abebeaedeac'))

from itertools import combinations

def solution2(arr, k, t):
  answer = 0
  temp_arr = []
  for i in range(k, len(arr)+1):
    temp_arr += combinations(arr, i)
  
  for temp_set in temp_arr:
    if sum(temp_set) <= t:
      answer += 1

  return answer

print(solution2([2,5,3,8,1],3,11))

select id, name, salaty bran