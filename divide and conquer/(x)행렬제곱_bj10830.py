# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
def mtp(mtx_a, mtx_b, n):
    idx = 0
    rst = [[0]*n for _ in range(n)]
    while idx < n:
        for i in range(n):
            for j in range(n):
                rst[i][j] += mtx_a[i][idx] * mtx_b[idx][j]
        idx += 1
    return rst

def sol(a, b, n):
    if b == 1:
        return a
    if b % 2:
        # r = sol(a, b//2, n)
        return mtp(mtp(sol(a, b//2, n), sol(a, b//2, n), n), a, n)
    else:
        # r = sol(a, b//2, n)
        return mtp(sol(a, b//2, n), sol(a, b//2, n), n)
n, b = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]
print(sol(mtx, b, n))
