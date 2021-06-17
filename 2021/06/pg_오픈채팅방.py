# 프로그래머스 2단계 오픈채팅방
# 2019년 카카오 공채 출제문제

import sys
input = sys.stdin.readline

def solution(record):
  log = []
  uid = {}
  for com in record:
    x = com.split(" ")
    if x[0] == "Enter":
      uid[x[1]] = x[2]
      log.append([x[0], x[1]])
    elif x[0] == "Leave":
      log.append([x[0], x[1]])
    else: # "Change"일 경우
      uid[x[1]] = x[2]

  answer = []
  for tmp in log:
    if tmp[0] == "Enter":
      a = f"{uid[tmp[1]]}님이 들어왔습니다."
    else:
      a = f"{uid[tmp[1]]}님이 나갔습니다."
    answer.append(a)
  return answer


print(solution(["Enter uid1234 Muzi", 
"Enter uid4567 Prodo",
"Leave uid1234",
"Enter uid1234 Prodo",
"Change uid4567 Ryan"]))