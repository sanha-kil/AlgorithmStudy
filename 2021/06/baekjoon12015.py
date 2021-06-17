# 백준 12015번 문제 LIS2

import sys
input = sys.stdin.readline
  
n = int(input()) 
a = list(map(int, input().split())) 
arr = [0] 

for x in a:
  start, end = 1, len(arr)-1
  while start < end:
    mid = (start+end)//2 
    if arr[mid] < x: 
      start = mid+1 
    elif arr[mid] > x: 
      end = mid 
    else: 
      start = end = mid 
  
  if arr[-1] < x: 
    arr.append(x) 
  else: 
    arr[start] = x 

print(len(arr)-1)