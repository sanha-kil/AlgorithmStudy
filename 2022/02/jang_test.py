def solution(numbers, start, finish):
  answer = []
  prefix_sum = [0]
  for i in range(len(numbers)):
    prefix_sum.append(numbers[i]+prefix_sum[i])
  for i in range(len(start)):
    answer.append(prefix_sum[finish[i]+1] - prefix_sum[start[i]])

  return answer
  
# print(solution([100, 101, 102,103, 104], [1, 2], [2, 4]))

def solution2(diet):
  answer = []
  for i in range(len(diet[0])):
    arr = [diet[0][i]]
    prev_idx = i
    for today in diet[1:]:
      dict = {}
      for j in range(len(today)):
        dict[today[j]] = j

      sorted_dict = sorted(dict.items())
      for x in sorted_dict:
        if prev_idx - x[1] >= 0:
          prev_idx = x[1]
          arr.append(x[0])
          break
    answer.append(sum(arr))

  return min(answer)

print(solution2([[360, 138, 338], [230, 102, 311], [320, 474, 214], [131, 498, 484], [366, 176, 249], [323, 407, 116], [265, 433, 317]]))

def solution3():
  return 0