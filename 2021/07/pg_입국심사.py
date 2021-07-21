# 프로그래머스 3단계 "압국심사"
# 코딩테스트 고득점 Kit 포함 문제

# n명을 심사하는 최소의 시간을 찾아야 함
# 최적의 시간을 찾을 때 까지 이분 탐색 반복
def solution(n, times):
  # 1과 최악의 시간(모두가 가장 시간이 오래걸리는 심사관에게 심사를 받을경우)을 좌, 우로 설정
  start, end = 1, n * max(times)

  # 이분 탐색 시작
  while start <= end:
    # mid = 심사관에게 주어진 시간
    mid = (start+end) // 2

    # mid값 안에서 각 심사관이 심사할 수 있는 사람의 수 확인
    count = 0
    for x in times:
      count += mid // x
    
    # 현 mid값에서 심사관이 n보다 많은 사람들을 심사할 수 있을 경우
    # end값을 줄여 범위를 하향 조정한다
    if count >= n:
      end = mid -1
      answer = mid
    # 현 mid값에서 심사관이 n보다 적은 사람들을 심사할 수 있을 경우
    # start값을 높여 범위를 상향 조정한다
    else:
      start = mid + 1
  
  return answer

print(solution(6, [7,10]))