const solution = (vote) => {
  const obj = { A: 0, B: 0, C: 0 };
  for (i of vote) {
    obj[i] += 1;
  }
  const MAX = Math.max(...Object.values(obj));

  let answer = "";
  for (x in obj) {
    if (obj[x] === MAX) answer += x;
  }

  if (answer.includes("C")) return answer.slice(0, -1);
  else return answer;
};

const VOTE = "AAAABBCCCCCBBAB";
console.log(solution(VOTE));
