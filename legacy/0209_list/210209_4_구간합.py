# import sys
# sys.stdin = open("sample_input (3).txt")
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    total_list = []
    for i in range(n-m+1):
        m_total = 0
        for j in range(i, i+m):
            m_total += nums[j]
        total_list.append(m_total)

    for a in range(len(total_list)):
        for b in range(len(total_list) - 1):
            if total_list[b] > total_list[b+1]:
                total_list[b], total_list[b+1] = total_list[b+1], total_list[b]
    rst = total_list[-1] - total_list[0]

    print('#{} {}'.format(tc, rst))

