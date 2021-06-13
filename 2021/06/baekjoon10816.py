# 백준 10816번 숫자카드2


# 이분 탐색 활용 방법
# import sys
# input = sys.stdin.readline

# def bin_search(m, nums):
#   if len(nums) <= 2:
#     return nums.count(m)

#   mid = len(nums) // 2
#   if m == nums[mid]:
#     return nums.count(m)
#   elif m < nums[mid]:
#     return bin_search(m, nums[:mid])
#   else:
#     return bin_search(m, nums[mid+1:])

  

# n = int(input())
# n_list = sorted(list(map(int, input().split())))
# m = int(input())
# m_list = list(map(int, input().split()))

# answer = []
# for x in m_list:
#   answer.append(bin_search(x, n_list))

# print(' '.join(str(x) for x in answer))


# 딕셔너리를 이용한 해싱 알고리즘

import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

hashtable = {}

for x in n_list:
  if x in hashtable:
    hashtable[x] +=1
  else:
    hashtable[x] = 1

print(' '.join(str(hashtable[x]) if x in hashtable else '0' for x in m_list))