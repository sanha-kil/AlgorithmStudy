def hopscotch(land):
    array=[]
    for i in range(0, 4):
        k = land
        tmp = i
        p = k[0][i]
        for j in range(1, len(land)):
            k[j][tmp] = 0
            p += max(k[j])
            tmp = k[j].index(max(k[j]))
        array.append(p)
    answer = max(array)
    return answer