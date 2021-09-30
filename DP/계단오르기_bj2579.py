import sys
input = sys.stdin.readline
n = int(input())
f = [0]
for _ in range(n):
    f.append(int(input()))
dl = [[0]*(n+1) for _ in range(2)]
def dp(i):
    # 0: 전전 / 1: 전
    dl[0][1], dl[1][1] = f[1], 0
    for i in range(2, n+1):
        dl[0][i] = max(f[i]+dl[0][i-2], f[i]+dl[1][i-2])
        dl[1][i] = f[i] + dl[0][i-1]
dp(n)
print(max(dl[0][n], dl[1][n]))