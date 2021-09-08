def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d:
        answer += i
        cnt += 1
        if answer == budget:
            return cnt
        elif answer > budget:
            return cnt-1
    else:
        return cnt