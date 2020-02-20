# 하노이의 탑 알고리즘
# 재귀 이용하면 개쉬움

answer=[]

def hanoi(n, st, mid, des):
    if n == 1:
        answer.append([st,mid])
        return
    else:
        hanoi(n-1, st, des, mid)
        answer.append([st, mid])
        hanoi(n-1, mid, st, des)

if __name__ == "__main__":
    hanoi(int(input("n = ")), 1, 2, 3)
    print(answer)