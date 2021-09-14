import sys
sys.stdin = open('sample_input (전자카트).txt')

def perm(v, d):
    global perm_arr
    global visited
    perm_arr[d] = v
    visited[v] = 1
    # 순열 완성될때마다
    if d == n-1:
        sol(perm_arr, 0)
        return
    for i in range(1, n+1):
        if not visited[i]:
            perm(i, d+1)
            visited[i] = 0

def sol(p, sum_v):
    global min_sum
    for i in range(n-1):
        sum_v += arr[perm_arr[i]-1][perm_arr[i+1]-1]
        # 합계가 최소값 넘어버리면 바로 리턴
        if sum_v > min_sum:
            return
    # 마지막 1로 가는거 처리
    sum_v += arr[perm_arr[-1]-1][0]
    # min_sum 보다 sum이 작으면 교체
    if min_sum > sum_v:
        min_sum = sum_v
    return

t = int(input())
for tc in range(1, t+1):
    # n줄
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 1~n 1로 시작하는 순열
    visited = [0] * (n+1)
    p = [1]
    min_sum = 987654321
    perm_arr = [0] * n
    perm(1,0)
    print('#{} {}'.format(tc, min_sum))
