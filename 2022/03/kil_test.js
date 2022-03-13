function solution(money, costs) {
    let answer = 0;
    const c = [1,5,10,50,100,500]
    const check = [...c].reverse()
    const p = []


    for(let i = 0 ; i < costs.length; i++){
       p.push([c[i], check[i]*costs[i], costs[i]])
    }

    p.sort((a,b) => a[1] - b[1])

    for(let i=0; i < p.length; i++){
        if(money > 0){
        let temp = Math.floor(money / p[i][0])
            answer += (temp * p[i][2])
            money -= (temp * p[i][0])
        }
    }

    return answer;
}

console.log(solution(4578, [1, 4, 99, 35, 50, 1000]))

function factorial(n) {
    let result = 1;
    for(let i=2; i<=n; i++) result *= i;
    return result;
}

function checkCase(x, y){
    console.log(x,y)
    let result = factorial(x+y)/(factorial(x)*factorial(y))
    console.log('result', result)
    return result
}

function solution3(width, height, diagonals) {
    let answer = 0;
    for (k of diagonals){
        const xy = [[k[0]-1, k[1]],[k[0], k[1]-1]]
        console.log(xy)
        answer += checkCase(xy[0][0], xy[0][1]) * checkCase(width-xy[1][0], height-xy[1][1])
        answer += checkCase(xy[1][0], xy[1][1]) * checkCase(width-xy[0][0], height-xy[0][1])
        console.log('answer', answer)
    }
    
    return answer % 10000019;
}

// console.log(checkCase(34, 19))
// console.log(solution3(2,2,[[1,1],[2,2]]))
// console.log(solution3(51,37,[[17,19]]))