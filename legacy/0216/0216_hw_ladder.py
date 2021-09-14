import sys
sys.stdin = open("input (hw).txt")

t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if arr[99][i] == 2:
            start = i
    c = start
    r = 99
    while r > 0:
        if c < 99 and arr[r][c + 1]:
            while c < 99 and arr[r][c + 1]:
                c += 1
            else:
                r -= 1
        elif c > 0 and arr[r][c - 1]:
            while c > 0 and arr[r][c - 1]:
                c -= 1
            else:
                r -= 1
        else:
            r -= 1
    rst = c
    print('#{} {}'.format(tc, rst))


