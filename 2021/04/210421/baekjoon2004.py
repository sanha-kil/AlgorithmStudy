import sys
input = sys.stdin.readline

def counting(num, k):
  count = 0
  while(num != 0):
    num //= k
    count += num
  return count

n, m = map(int, input().split())
print(min(counting(n,2)-counting(m,2)-counting(n-m,2), counting(n,5)-counting(m,5)-counting(n-m,5)))