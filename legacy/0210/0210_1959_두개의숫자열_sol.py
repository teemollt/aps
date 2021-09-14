import sys
sys.stdin = open("input (2).txt")

def check(long, short):
    max_v = -987654321
    for i in range(len(long)-len(short)+1):
        rst = 0
        for j in range(len(short)):
            rst += long[i+j] * short[j]

        if max_v < rst:
            max_v = rst

    return max_v


t = int(input())
for tc in range(1, t+1):
    # 입력
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        ans = check(a, b)
    else:
        ans = check(b, a)

    print('#{} {}'.format(tc, ans))