def solution(info, query):
    itmp = []
    qtmp = []
    for i in range(len(info)):
        itmp.append(info[i].split())
        qtmp.append(query[i].split(" and "))
        qtmp[i]= qtmp[i] + (qtmp[i].pop()).split()
    answer = []
    for i in range(len(qtmp)):
        count = 0
        for j in range(len(itmp)):
            for k in range(5):
                if k != 4:
                    if qtmp[i][k] == '-' or itmp[j][k] == qtmp[i][k]:
                        continue
                    else:
                        break
                else:
                    if int(itmp[j][k]) >= int(qtmp[i][k]):
                        count = count + 1
        answer.append(count)
    return answer


x= ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
y = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(x, y))