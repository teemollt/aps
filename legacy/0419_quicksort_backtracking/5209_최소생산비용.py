import sys
sys.stdin = open("sample_input (minpro).txt")

def min_cost(idx, d, sum_c):
    global min_c
    if d == n:
        if min_c > sum_c:
            min_c = sum_c
        return
    elif min_c <= sum_c:
        return
    for i in range(n):
        if not used[i]:
            used[i] = 1
            min_cost(idx+1, d+1, sum_c+arr[idx][i])
            used[i] = 0



t = int(input())
for tc in range(1, t+1):
    # 제품수 n
    n = int(input())
    # 생산비용
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * n
    min_c = 987654321
    min_cost(0, 0, 0)
    print('#{} {}'.format(tc, min_c))