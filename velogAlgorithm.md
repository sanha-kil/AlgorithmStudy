## 벨로그 알고리즘 문제 풀이 작성을 위한 마크다운 양식

>
### 문제
[백준 번 ](https://www.acmicpc.net/problem/)

***
### 풀이



***
### Python 코드

```python

```

>
### 문제
[백준 1992번 쿼드트리](https://www.acmicpc.net/problem/1992)

***
### 풀이
쿼드트리를 이용한 분할 정복 문제.

[2630번](https://velog.io/@kgpaper/%EB%B0%B1%EC%A4%80-2630%EB%B2%88-%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0)과 전체적으로 비슷한 문제지만 다른점이 있다면,
4분면으로 나누고 재귀에 들어가기 전, 괄호를 열고 해당 순서의 재귀가 끝나면 괄호를 닫아주어야 한다.


***
### Python 코드

```python
import sys
input = sys.stdin.readline

def quad_tree(p, n):
  check = p[0][0]
  ex = False

  for i in range(n):
    if ex:
      break

    for j in range(n):
      if p[i][j] != check:
        print('(', end='')
        quad_tree([row[:n//2] for row in p[:n//2]], n//2)
        quad_tree([row[n//2:n] for row in p[:n//2]], n//2)
        quad_tree([row[:n//2] for row in p[n//2:n]], n//2)
        quad_tree([row[n//2:n] for row in p[n//2:n]], n//2)
        ex = True
        print(')', end='')
        break
    
  if not ex:
    print(check, end='')

n = int(input())
paper = []
for i in range(n):
  paper.append(input().strip())

quad_tree(paper, n)
```