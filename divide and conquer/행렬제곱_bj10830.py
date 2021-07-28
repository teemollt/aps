# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
def mtp(mtx, n):
    idx = 0
    rst = [[0]*n for _ in range(n)]
    while idx < n:
        for i in range(n):
            for j in range(n):
                rst[i][j] += mtx[i][idx] * mtx[idx][j]
        idx += 1
    return rst

def sol(a, b):
    if b == 1:
        return a
    if b % 2:
        return sol(mtp(mtx,n), b//2)) * a
    else:
        return sol(a, b//2)

n, b = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]
print(mtp(mtx, n))