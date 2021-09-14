import sys
sys.stdin = open("sample_input (4881).txt")

def sol(sum):
    # 열 방문처리 해줘야됨
    global visited1
    global visited2
    global min
    # 시간위해서
    if sum > min:
        return
    # idx가 n과 같아지면 마지막 행까지 한거
    # if idx == n:
    #     if min > sum:
    #         min = sum
    cnt = 1
    for i in range(n):
        cnt *= visited1[i]
    if cnt:
        if min > sum:
            min = sum
    # 행 돌기
    for i in range(n):
        # 방문처리된 열은 X
        for j in range(n):
            if not visited1[i] and not visited2[j]:
                visited1[i] = 1
                visited2[j] = 1
                sol(sum+arr[i][j])
                visited1[i] = 0
                visited2[j] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    # 열 겹치면 안되니까
    visited1 = [0] * n
    visited2 = [0] * n
    # 바로 최소합 검사위해서
    min = 987645321
    sol(0)
    print('#{} {}'.format(tc, min))