# 프로그래머스 2단계 "다리를 지나는 트럭"
# 코딩테스트 고득점 Kit 포함

from collections import deque

def solution(bridge_length, weight, truck_weights):
  time = 1
  truck = deque(truck_weights)
  on_bridge = deque([truck.popleft()])
  cross = deque([0])
  while 1:
    time += 1
    print(time)

    for i in range(len(on_bridge)):
      cross[i] += 1

    if cross[0] == bridge_length:
      cross.popleft()
      on_bridge.popleft()

    if truck and (sum(on_bridge) + truck[0]) <= weight and len(on_bridge) < bridge_length:
      on_bridge.append(truck.popleft())
      cross.append(0)

    if not on_bridge:
      return time


print(solution(100,100,[10]))