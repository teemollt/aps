def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    l, r = 0, distance
    while l <= r:
        minv = 1e10
        mid = (l+r)//2
        pre = 0
        rmv = 0
        for i in range(len(rocks)):
            if rocks[i] - pre < mid:
                rmv += 1
            else:
                minv = min(minv, rocks[i]-pre)
                pre = rocks[i]
        if rmv > n:
            r = mid - 1
        else:
            answer = minv
            l = mid + 1
    return answer