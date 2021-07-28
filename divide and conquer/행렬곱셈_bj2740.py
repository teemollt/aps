an, am = map(int, input().split())
mat_a = [list(map(int, input().split())) for _ in range(an)]
bn, bm = map(int, input().split())
mat_b = [list(map(int, input().split())) for _ in range(bn)]
rst = [[0]*bm for _ in range(an)]
idx = 0
while idx < am:
    for i in range(an):
        for j in range(bm):
            rst[i][j] += mat_a[i][idx] * mat_b[idx][j]
    idx += 1
for i in range(an):
    for j in range(bm):
        print(rst[i][j], end=" ")
    print()
