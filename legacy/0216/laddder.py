import sys
sys.stdin = open("input (hw).txt")

t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if arr[0][i]:
            start.append(i)

    for i in start:
        c = i
        r = 0
        while r < 99:
            if c < 99 and arr[r][c + 1]:
                while c < 99 and arr[r][c + 1]:
                    c += 1
                else:
                    r += 1
            elif c > 0 and arr[r][c - 1]:
                while c > 0 and arr[r][c - 1]:
                    c -= 1
                else:
                    r += 1
            else:
                r += 1
                if arr[r][c] == 2:
                    rst = i
    print('#{} {}'.format(tc, rst))