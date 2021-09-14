import sys
sys.stdin = open("sample_input (화물도크).txt")
#
# def sol(idx, cnt):
#     global used, max_c
#     used[idx] = 1
#     # if idx == n-1:
#     #     if max_c < cnt:
#     #         max_c = cnt
#     #     return
#     if cnt == n or cnt == 24 - time[0][1]:
#         return
#     for i in range(n):
#         if time[idx][1] <= time[i][0] and used[i] == 0:
#             sol(i, cnt+1)
#             used[i] = 0
#     if max_c < cnt:
#         max_c = cnt
# 전부다 구해서 비교하면 시간초과됨 그리디로 풀어야함.
# 그리디로 풀어도 항상 옳다는거 증명해야함...
t = int(input())
for tc in range(1, t+1):
    # 신청서 n
    n = int(input())
    # 시작시간 s 종료시간 e
    time = [list(map(int, input().split())) for _ in range(n)]
    # 종료시간 빠른순 정렬
    for i in range(n):
        fast = i
        for j in range(i, n):
            if time[fast][1] > time[j][1]:
                fast = j
        time[fast], time[i] = time[i], time[fast]
    cnt = 1
    used = []
    for i in range(n):
        if used:
            if used[-1] > i:
                continue
        for j in range(i, n):
            if time[i][1] <= time[j][0]:
                cnt += 1
                used.append(j)
                break
    print('#{} {}'.format(tc, cnt))
