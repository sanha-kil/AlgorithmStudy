import sys
input = sys.stdin.readline

def bin_search(l, k):
  left = 0
  right = len(l) - 1

  while left <= right:
    mid = (left+right)//2
    if k == l[mid]:
      return 1
    elif k > l[mid]:
      left = mid+1
    else:
      right = mid-1
  return 0

n = int(input())
nlist = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))
for i in range(m):
  print(bin_search(nlist, mlist[i]))

