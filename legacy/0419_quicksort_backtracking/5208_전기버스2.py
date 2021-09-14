import sys
sys.stdin = open("sample_input (bus2).txt")

t = int(input())
for tc in range(1, t+1):
    # 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    m = arr + [0]
    # print(n, m)
    # 뒤에서부터 돌아서 가장 멀리서 현위치에 도달할 수 있는곳 찾기
    # 현위치까지 오는데 필요한 용량 power
    ci = n-1
    cnt = 0
    while ci > 0:
        power = 1
        for i in range(ci-1, -1, -1):
            if m[i] >= power:
                ci = i
            power += 1
        cnt += 1
    print('#{} {}'.format(tc, cnt-1))
