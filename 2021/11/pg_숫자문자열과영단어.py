# 프로그래머스 Level1 '숫자 문자열과 영단어'
# 21년도 카카오 채용형인턴 선발 문제


def solution(s):
  answer = ''
  temp = ''         # 영단어 저장을 위한 
  dict = {          # 해시알고리즘을 위한 딕셔너리 선언
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
  }
    
  for i in s: 
    if i in '0123456789':     # 숫자가 나오면 정답에 바로 넣어줌
      answer += i
    else:
      temp += i
      
    if temp in dict:          # 쌓여있는 문자열이 dict 안에 있는 경우
      answer += dict[temp]    # 그에 해당하는 숫자 정답에 넣고 temp 초기화
      temp=''
    
  return int(answer)