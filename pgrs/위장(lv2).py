# 정답코드
def solution(clothes):
    answer = 1
    d = {}
    for i in clothes:
        if i[1] in d:
            d[i[1]] += 1
        else:
            d[i[1]] = 1
    cnt = list(d.values())
    # 각 종류별로 해당 종류를 안입는 경우를 +1 해서 모두 곱하고
    for i in cnt:
        answer *= (i+1)
    # 모든 경우의수에서 모든 종류를 다 안입는 경우 -1을 해주면 정답
    return answer-1


# 1번 케이스 시간초과 나는 방식 모든 경우의수를 구해서 더해줌
import itertools
def solution(clothes):
    answer = 0
    d = {}
    for i in clothes:
        if i[1] in d:
            d[i[1]] += 1
        else:
            d[i[1]] = 1
    def mtp(li):
        rst = 1
        for i in li:
            rst *= i
        return rst
    cnt = list(d.values())
    for i in range(len(cnt)):
        comb = list(itertools.combinations(cnt, i+1))
        for j in comb:
            answer += mtp(j)
    return answer