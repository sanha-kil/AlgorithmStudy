import sys
input = sys.stdin.readline

def cut(x,y,n):
    global m_one,zero,one
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                #9등분하기
                for a in range(3):
                    for b in range(3):
                        cut(x+n//3*a,y+n//3*b,n//3)
                return
 
    if check==-1:
        m_one+=1
    elif check==0:
        zero+=1
    elif check==1:
        one+=1

n = int(input())
paper = []
one = 0
zero = 0
m_one = 0
for _ in range(n):
  paper.append(list(map(int, input().split())))

cut(0, 0, n)

print(m_one)
print(zero)
print(one)