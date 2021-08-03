# 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
from sys import stdin
n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))
trees.sort()
l, r = 0, trees[-1]
rst = 0
while l <= r:
    mid = (l+r)//2
    gt = 0
    for tree in trees:
        if mid < tree:
            gt += (tree - mid)
    if gt >= m:
        rst = mid
        l = mid+1
    else:
        r = mid-1
print(rst)