
from itertools import combinations

def bsum(arr):
  first = arr[0]
  last = arr[-1]
  start_idx = 0
  end_idx = len(arr)-1
  while start_idx+1 != end_idx-1:
    if first < last:
      start_idx += 1
      first += arr[start_idx]
    else:
      end_idx -= 1
      last += arr[end_idx]

    print(first, last)

  return start_idx + 1


# print(bsum([1,2,3,3,1,8,9,1]))

def sel_sort(a):
  n = len(a)
  for i in range(0, n - 1):
    min_idx = i
    for j in range(i + 1, n):
      if a[j] < a[min_idx]:
        min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
    print(a)     # 정렬 과정 출력하기

# print(sel_sort([2, 4, 5, 1, 3]))

def solution(num):
  n = int('1'+'0'*(num-1))
  result = int(n**0.5)-1

  while result:
    if result**2 >= n:
      break
    else:
      result += 1
  return result


# print(solution(2))

def ParallelSums(arr):
  if sum(arr) % 2 == 1:
    return -1

  target = int(sum(arr)/2)
  adjustedArr = list(combinations(arr, int(len(arr)/2)))
  for a in adjustedArr:
    b = arr
    if sum(a) == target:
      for k in a:
        b.remove(k)
      
      a_answer = sorted(a)
      b_answer = sorted(b)

      if a_answer[0] <= b_answer[0]:
        return ','.join(map(str,a_answer+b_answer))
      else: 
        return ','.join(map(str,b_answer+a_answer))

  return -1
    
def compose(a,b):
  a.sort()
  b.sort()
  if a[0] <= b[0]:
    return ','.join(str(x) for x in a + b)
  else:        
    return ','.join(str(x) for x in b + a)

print(ParallelSums([16, 22, 35, 8, 20, 1, 21, 11]))