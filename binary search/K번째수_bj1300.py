# 이문제 역시 해당 값이 조건을 충족하는지 확인하는 과정 +
# 이분탐색으로 범위를 좁혀나가면서 시간을 단축
n, k = int(input()), int(input())
l, r = 1, k
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for i in range(1,n+1):
        v = mid//i
        if v > n:
            cnt += n
        else:
            cnt += v
    if cnt >= k:
        rst = mid
        r = mid-1
    else:
        l = mid+1
print(rst)

