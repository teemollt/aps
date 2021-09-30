n = int(input())
dp = [0,0,1,1] + [0] * (n-3)
def sol(i):
    if i < 4:
        return
    for i in range(4, n+1):
        dp[i] = dp[i-1]+1
        if not i % 3:
            dp[i] = min(dp[i], dp[i//3]+1)
        if not i % 2:
            dp[i] = min(dp[i], dp[i//2]+1)
sol(n)
print(dp[n])