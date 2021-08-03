# 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
# K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력
from sys import stdin
k, n = map(int, stdin.readline().split())
lines = [int(stdin.readline()) for _ in range(k)]
l, r = 1, sum(lines)//n
rst = 0
while l <= r:
    mid = (l+r) // 2
    cnt = 0
    for line in lines:
        cnt += line//mid
    if cnt >= n:
        l = mid+1
        rst = mid
    else:
        r = mid-1
print(rst)
