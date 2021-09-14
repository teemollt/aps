import sys
sys.stdin = open("sample_input (grouping).txt")

def sol(v):
    global in_group, cnt
    q = []
    used = [0] *(n+1)
    tmp = []
    # 그룹에 한번 들어갔던 사람이면 바로 리턴
    if in_group[v]:
        return
    # 아니면 인그룹에 체크해주고 확인
    q.append(v)
    used[v] = 1
    # 탐색
    while q:
        c = q.pop(0)
        tmp.append(c)
        for i in range(1, n+1):
            if arr[c][i]:
                if in_group[i]:
                    return
            # 검사한적 없는 사람 + 표 받은 사람이면
                elif arr[c][i] and not in_group[i] and not used[i]:
                    used[i] = 1
                    q.append(i)
    # 리턴 안되고 while문 통과했으면 새로운 그룹 +1
    # print('tmp {}'.format(tmp))
    cnt += 1
    for i in tmp:
        in_group[i] = 1

t = int(input())
for tc in range(1, t+1):
    # 1~n번 출석번호, m장의 신청서 제출 몇개의 조가 만들어지나?
    n, m = map(int, input().split())
    arr = [[0] * (n+1) for _ in range(n+1)]
    a = list(map(int, input().split()))
    for i in range(m):
        x, y = a[i*2], a[i*2+1]
        arr[x][y] = 1
        arr[y][x] = 1
    # print(arr)
    # 한번이라도 체크되면 이미 그룹에 포함된 인간
    in_group = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        sol(i)
    print('#{} {}'.format(tc, cnt))