import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
cnt = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    elif coins[i] <= k:
        cnt += k // coins[i]
        k %= coins[i]
print(cnt)