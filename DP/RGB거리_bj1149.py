from sys import stdin
input = stdin.readline
n = int(input())
dp = [[0]*3 for _ in range(n)]
for i in range(n):
    dp[i][0], dp[i][1], dp[i][2] = map(int, input().split())
def sol(n, dp):
    for i in range(1, n):
        dp[i][0] += min(dp[i-1][1], dp[i-1][2])
        dp[i][1] += min(dp[i-1][0], dp[i-1][2])
        dp[i][2] += min(dp[i-1][0], dp[i-1][1])
    return min(dp[n-1])
print(sol(n, dp))