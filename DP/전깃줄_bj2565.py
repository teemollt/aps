import sys
input = sys.stdin.readline
def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    dp = [1]*501
    for i in range(n):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                dp[arr[i][0]] = max(dp[arr[i][0]], dp[arr[j][0]]+1)
    print(n-max(dp))
sol()