function solution(n, computers) {
  const isVisited = [];
  let answer = 0;

  const dfs = (index) => {
    isVisited[index] = true;
    for (let i = 0; i < n; i++) {
      if (computers[index][i] && !isVisited[i]) dfs(i)
    }
  };

  for (let i = 0; i < n; i++) {
    if (!isVisited[i]) {
      dfs(i);
      answer += 1;
    }
  }

  return answer
}


console.log(solution([[1, 1, 0], [1, 1, 0], [0, 0, 1]]));