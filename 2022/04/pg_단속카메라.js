const solution = (routes) => {
  let answer = 0;
  let currentLocation = -30001;

  routes.sort((a, b) => a[1] - b[1]);

  for ([start, end] of routes) {
    if (currentLocation < start) {
      answer++;
      currentLocation = end;
    }
  }
  return answer;
};

console.log(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]));