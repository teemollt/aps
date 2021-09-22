def solution(answers):
    answer = [[0, 1],[0, 2],[0, 3]]
    s = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    n = len(answers)
    for i in range(n):
        if answers[i] == s[0][i%5]:
            answer[0][0] += 1
        if answers[i] == s[1][i%8]:
            answer[1][0] += 1
        if answers[i] == s[2][i%10]:
            answer[2][0] += 1
    answer.sort()
    c = 0
    for j in answer:
        if j[0] == answer[2][0]:
            c += 1
    if c == 1:
        answer = [answer[2][1]]
    elif c == 2:
        answer = [answer[1][1], answer[2][1]]
    elif c == 3:
        answer = [answer[0][1], answer[1][1], answer[2][1]]
    return answer