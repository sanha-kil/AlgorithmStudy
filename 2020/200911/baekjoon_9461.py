'''
    백준 9461번 파도반 수열문제.
    plist = [1,1,1,2,2,3,4,5,7,9,12,....]
    수열을 분석해보면 P(n) = P(n-1) + P(n-5)인걸 알 수 있다.
'''

def pado(x):
    plist = [0,1,1,1,2,2,3]
    for i in range(7, x+1):
        plist.append(plist[i-1]+plist[i-5])
    return plist[x]

for _ in range(int(input())):
    print(pado(int(input())))