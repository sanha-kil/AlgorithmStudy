# 프로그래머스 4단계 "징검다리"
# 코딩테스트 고득점 Kit 포함 문제
# 이분 탐색

def solution(distance, rocks, n):
  answer = 0
  # 시작지점은 0, end값은 도착지점으로 설정
  start, end = 0, distance

  # 각 돌 사이 거리를 재기 위한 정렬
  rocks.sort()

  # 이분 탐색 진행
  while start <= end:
    mid = (start+end) // 2
    
    # 앞에 있는 돌
    tmp = 0
    # 제거한 돌
    count = 0

    for x in rocks:
      # 돌 사이의 거리가 mid값보다 적을경우 제거
      if x - tmp < mid:
        count += 1

      # 반대일 경우 x(현재시점에서 비교하는 돌)을 tmp(기준이 되는 돌)로 설정
      else:
        tmp = x
    
    # 제거된 돌이 n보다 많으면 범위를 하향조정 한다
    if count > n:
      end = mid-1
    # 반대일 경우 범위를 상향조정한다.
    else:
      answer = mid
      start  = mid + 1

  return answer