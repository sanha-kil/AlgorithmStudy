# 프로그래머스 2단계 "전화번호 목록"

def solution(phone_book):
  book = sorted(phone_book)
  for i in range(len(book)-1):
    if book[i+1].startswith(book[i]):
      return False
  return True

solution(["12","123","1235","567","88"])