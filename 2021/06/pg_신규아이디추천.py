import re

def solution(new_id):
  answer = str(new_id)
  
  # 1단계
  answer = answer.lower()
  
  #2딘계
  answer = re.sub("[^a-z0-9-_.]", "", answer)
  
  #3단계
  answer = re.sub('\.\.+','.',answer)

  #4단계
  answer = re.sub('^\.|\.$','', answer)

  #5단계
  if not answer:
      answer = 'a'

  #6단계
  answer = re.sub('\.$', '', answer[:15])

  #7단계
  while len(answer) < 3:
      answer += answer[len(answer)-1]
  return answer