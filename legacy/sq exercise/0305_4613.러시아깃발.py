import sys
sys.stdin = open("sample_input (4613).txt")

# idx는 각 색을 몇개 줄에 칠하는지를 저장하는 리스트 idx, sum은 각 줄 수 합
def sol(idx, sum):
    # 색깔별 줄수 담을 c 변경할거니까
    global c
    global rst
    # 유망한지 확인 sum이 n보다 클수 없으니 그만
    if sum > n:
        return
    # 색깔 3개까지니까 idx는 2까지 가능 3이면 그만
    if idx == 3:

        cnt = 0
        # 흰색 칠하기 0~c[0]-1
        for i in range(c[0]):
            for j in range(m):
                if arr[i][j] != 'W':
                    cnt += 1
        # 파랑 칠하기 c[0] ~ c[1]-1
        for i in range(c[0], c[0]+c[1]):
            for j in range(m):
                if arr[i][j] != 'B':
                    cnt += 1
        # 빨강 c[1]+1 ~ n
        for i in range(c[0]+c[1], n):
            for j in range(m):
                if arr[i][j] != 'R':
                    cnt += 1

        if cnt < rst:
            rst = cnt
        return
    # 각각 최소 1줄이니까 각 줄을 칠할수 있는 경우의수는 1~n-2
    # 이걸 반복문 돌면서 모든 경우의수 재귀로 다른색깔도 불러와
    for i in range(1, n-1):
        c[idx] = i
        sol(idx + 1, sum + i)

t = int(input())
for tc in range(1, t+1):
    # n행 m열
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    # print(arr)
    # 각 줄을 칠하는 경우의수 넣어줄 리스트
    c = [0] * 3
    rst = 987654321
    sol(0, 0)
    print('#{} {}'.format(tc, rst))
