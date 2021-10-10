import sys
input = sys.stdin.readline
# 공통부분 수열 => 순서도 지켜져야됨
def sol():
    arr1, arr2 = input().rstrip(), input().rstrip()
    n, m = len(arr1), len(arr2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    # dp = [0]*(m+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr1[i-1] == arr2[j-1]:
                # dp[i][j] = dp[i-1][j-1]
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])
sol()


''' 아래 방법으로 1차원 배열 dp로도 가능
words1 = input()
words2 = input()
dp = [0] * len(words2)
for i in range(len(words1)):
    max_dp = 0
    for j in range(len(words2)):
        if max_dp < dp[j]:    
            max_dp = dp[j]
        elif words1[i] == words2[j]:
            dp[j] = max_dp + 1

print(max(dp))
'''