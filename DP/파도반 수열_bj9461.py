dp = [0,1,1,1,2,2,3,4,5,7,9] + [0]*90
def sol(n):
    for i in range(11, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[n]
t = int(input())
for tc in range(t):
    n = int(input())
    print(sol(n))
