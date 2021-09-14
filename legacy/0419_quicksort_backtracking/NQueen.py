# import sys
# sys.stdin = open("sample_input (queen).txt")

def queen(idx, d):
    global arr, cnt
    # 종료 조건
    if d == n:
        cnt += 1
        return
    # 가로줄이 같으면
    elif
    for j in range(n):
        if not arr[idx][j]:
            queen(idx+1, d+1)
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 체스판
    arr = [[0]*n for _ in range(n)]
    cnt = 0
    # 좌상부터 시계
    # dx = [-1, 1, 1, -1]
    # dy = [-1, -1, 1, 1]
    queen(0,0,0)
    print(cnt)
