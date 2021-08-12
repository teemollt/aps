n = 6
times = [7, 10]

def sol(n, times):
    l, r = 0, n*times[-1]
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for i in times:
            cnt += mid // i
        if cnt >= n:
            r = mid - 1
        else:
            l = mid + 1
            # total == n 일경우는 왼쪽 구간을 취해 최소값이 있는 구간을 취한다.
            answer = l
    return answer
print(sol(n, times))