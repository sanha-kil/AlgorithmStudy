function solution(M, load) {
    const arr = [];
    const sortedLoad = load.sort((a, b) => b-a);
    for (let payload of sortedLoad) {
        if (payload <= M) {
            if (arr.length === 0) {
                arr.push(payload)
                continue
            } else {
                for (let i=0; i < arr.length; i++){
                    let temp = payload + arr[i]
                    if(temp <= M) {
                        arr[i] = temp
                        break
                    }
                    if(i === arr.length-1){
                        arr.push(payload)
                        break
                    }
                }
            }
        }
    }

    answer = arr.length === 0 ? -1 : arr.length;
    return arr;
}

console.log(solution(20,[16,15,9,17,1,3]))