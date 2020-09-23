import re

def solution(new_id):
    answer = str(new_id)
    answer = answer.lower()
    answer = re.sub("[^a-z0-9-_.]", "", answer)
    print(answer)
    i = 1
    while i < len(answer):
        if len(answer) > 1:
            if answer[i] == answer[i-1] and answer[i] == ".":
                 answer = answer[:i] + "" + answer[i+1:]
            i=i+1
    answer = answer.strip(".")
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[0:16]
    answer = answer.strip(".")
    if len(answer) < 3:
        for i in range(len(answer), 3):
            answer = answer + answer[i-1]
    return answer

print(solution(str(input())))
