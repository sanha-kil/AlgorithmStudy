import sys

l = []
answer = []
for _ in range(int(input())):
    l.append(int(input()))

answer.append(l[0])
answer.append(max(l[0]+l[1], l[1]))
answer.append(max(l[0]+l[2], l[1]+l[2]))
for i in range(3, len(l)):
    answer.append(max(answer[i-2] + l[i], answer[i-3]+l[i-1]+l[i]))

print(answer.pop())

'''
백준 2579 계단오르기 문제.
두번의 연속되는 계단을 밟지 못한다는 조건을 생각해야 한다.
즉, i-1 계단을 밟았다면 i-3 계단에서 올라온 것이므로 i-3 계단까지의 가중치를 더해야하며, 
i-2 계단을 밟았다면 i-2 계단까지의 가중치를 더해야한다. 
answer[i] = max(l[i]+answer[i-2], l[i-1]+l[i]+answer[i-3])
정답은 맞췄으나 사이트 오류인지 내 코드뿐만아니라 구글에 올라와있는 정답 코드까지 런타임 오류를 뱉고 있다.
'''
