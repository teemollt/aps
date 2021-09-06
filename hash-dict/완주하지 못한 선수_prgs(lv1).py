# 딕셔너리의 키밸류쌍을 반환하는 items() 잘 기억이 안나더라..
def solution(participant, completion):
    d = {}
    for i in participant:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in completion:
        if i in d:
            d[i] -= 1
        else:
            return i
    for k, v in d.items():
        if v:
            return k

# 좋아요가 많이 박힌 풀이를 보면 collections 모듈의 Counter를 사용해서 아주 간단하게 풀이함.
# counter 객체끼리는 마이너스 연산이 가능하다?!
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
# hash 함수를 사용한 신박한 풀이도 있었음...
# 두리스트를 정렬해서 같은 인덱스끼리 비교하는 방식도 간단
