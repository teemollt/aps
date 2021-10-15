import sys
input = sys.stdin.readline
def sol():
    k = int(input())
    s = list(map(int, input().split()))
    n = len(s)
    arr = [[0]*n for _ in range(n)]
    inf = int(1e9)
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            min_v = inf
            for k in range(j-i):
                min_v = min(min_v, arr[i][i+k] + arr[i+k+1][j])
            arr[i][j] = min_v + sum(s[i:j+1])
    print(arr[0][n-1])
t = int(input())
for _ in range(t):
    sol()