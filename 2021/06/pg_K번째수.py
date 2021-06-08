def solution(array, commands):
    answer = []
    for a in commands:
      i = a[0]
      j = a[1]
      k = a[2]
      tmp = sorted(array[i-1:j])
      answer.append(tmp[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))