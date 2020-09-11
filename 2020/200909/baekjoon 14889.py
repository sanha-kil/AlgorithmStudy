from itertools import combinations
import sys

n = int(sys.stdin.readline())
mat = []
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

gab = 999999999
team = [i for i in range(n)]
tt = list(combinations(team, n // 2))
for team1 in tt:
    team2 = [x for x in team if x not in team1]
    team1_score = 0
    team2_score = 0
    for x, y in list(combinations(team1, 2)):
        team1_score += mat[x][y] + mat[y][x]
    for x, y in list(combinations(team2, 2)):
        team2_score += mat[x][y] + mat[y][x]
    gab = min(gab, abs(team1_score - team2_score))

print(gab)

'''
itertools의 combinations를 이용해 각 팀을 조합 구성한다.
이 후 두개로 나눠진 팀내에서 다시한번 combinations를 사용해 
2명씩 조합구성하여 각 경우의 수마다 값의 차이를 구하고 기존의 차이값과 비교
'''