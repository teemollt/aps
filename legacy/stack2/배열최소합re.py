import sys
sys.stdin = open("sample_input (4881).txt")

def sol(idx, sum):
    # 열 방문처리 해줘야됨
    global visited
    global min
    # 시간위해서
    if sum > min:
        return
    # idx가 n과 같아지면 마지막 행까지 한거
    if idx == n:
        if min > sum:
            min = sum
        return
    # 행 돌기
    for i in range(n):
        # 방문처리된 열은 X
        if not visited[i]:
            # 방문처리해주고 다음줄 ㄱㄱ
            visited[i] = 1
            sol(idx+1, sum+arr[idx][i])
            # 방문처리 취소
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    # 열 겹치면 안되니까
    visited = [0] * n
    # 바로 최소합 검사위해서
    min = 987645321
    sol(0, 0)
    print('#{} {}'.format(tc, min))
