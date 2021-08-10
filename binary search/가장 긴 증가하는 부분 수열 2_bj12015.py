# lis
from sys import stdin
input = stdin.readline
def sol(v):
    l, r = 0, len(rst) - 1
    while l <= r:
        mid = (l+r) // 2
        if rst[mid] >= v:
            r = mid - 1
        else:
            l = mid + 1
    return l

n = int(input())
arr = list(map(int, input().split()))
rst = [0]
for i in arr:
    if i > rst[-1]:
        rst.append(i)
    else:
        rst[sol(i)] = i
print(len(rst)-1)

