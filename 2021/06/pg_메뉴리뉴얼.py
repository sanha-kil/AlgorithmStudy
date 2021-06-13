from itertools import combinations
from collections import Counter


def solution(orders, course):
    sets = [[] for _ in range(len(course))]
    for i in range(len(orders)):
        a = sorted(list(orders[i]))
        print(a)
        for j in range(len(course)):
            tmp=combinations(a, course[j])
            sets[j].extend(tmp)
    
    answer = []
    for i in range(len(course)):
        x = Counter(sets[i])
        print(x)
        answer = answer + [''.join(list(j)) for j, y in x.items() if y == max(x.values()) and y > 1]
    return sorted(answer)

tlist = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
c = [2,3,4]
print(solution(tlist, c))