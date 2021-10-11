import sys
input = sys.stdin.readline
def sol():
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
    print(max(dp[1:]))
sol()
