import sys
sys.stdin = open("input (jin).txt")
T = int(input())
for tc in range(1, T+1):
    # N명가능 M초동안 K개
    N, M, K = map(int, input().split())
    #  각 사람들이 도착하는 시간
    person = list(map(int, input().split()))
    # 정렬
    for i in range(len(person)-1):
        min = i
        for j in range(i+1, len(person)):
            if person[min] > person[j]:
                min = j
        person[i], person[min] = person[min], person[i]
    # print(person)
    # 시간 -> idx 빵이 나올때마다 bread에 + 사람들 도착할때마다 - 해서 음수가 되면 break하고 impossible
    bread = 0
    max_p = 0
    for i in person:
        if i > max_p:
            max_p = i
    # print(max_p)
    for idx in range(0, max_p+1):
        # 빵 추가
        if idx % M == 0 and idx != 0:
            bread += K
        # 사람 올때 파악 idx가 초이므로 사람이 올 시간 리스트에 idx가 포함이 되어있다면
        if idx in person:
            # 그 시간에 몇명이 올지 파악하고 그만큼 그시간에 bread에서 -해줌
            cnt = 0
            for i in range(len(person)):
                if person[i] == idx:
                    cnt += 1
            bread -= cnt
        if bread < 0:
            break
    if bread < 0:
        rst = 'Impossible'
    else:
        rst = 'Possible'
    print('#{} {}'.format(tc, rst))