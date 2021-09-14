import sys
sys.stdin = open("input (dongchung).txt")

def work(idx, d, p):
    global success
    if d == n:
        # 비교
        if success < p:
            success = p
        return
    elif success >= p:
        return
    for i in range(n):
        if not used[i]:
            used[i] = 1
            work(idx+1, d+1, p*arr[idx][i])
            used[i] = 0

t = int(input())
for tc in range(1, t+1):
    # 직원수, 일수 n
    n = int(input())
    # 성공확률 배열
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j] / 100
    # print(arr)
    success = 0
    used = [0] * n
    work(0, 0, 1)
    print('#{} {:6f}'.format(tc, success*100))

