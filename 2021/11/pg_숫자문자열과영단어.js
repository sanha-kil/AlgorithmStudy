const solution = (s) => {
  let answer = "";
  let temp = "";
  const dict = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  for (let x of s) {
    if ("0123456789".includes(x)) {
      answer += x;
    } else {
      temp += x;
    }
    if (temp in dict) {
      answer += dict[temp];
      temp = "";
    }
  }
  return Number(answer);
};
