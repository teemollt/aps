# import sys
# sys.stdin = open("sample_input (3).txt")
T = int(input())
for tc in range(1, T+1):
    # n : 원소의 개수
    # m : 구간의 길이
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    max_v = 0
    min_v = 987654321

    # 구간 시작점
    for i in range(n - m + 1):
        tmp = 0

        for j in range(m):
            tmp += nums[i + j]

        # 상동
        # for j in nums[i: i+m]:
        #   tmp += j
        if max_v < tmp:
            max_v = tmp

        if min_v > tmp:
            min_v = tmp

    print('#{} {}'.format(tc, max_v - min_v))

####################################풀이2 윈도우슬라이딩 알고리즘..##################

T = int(input())
for tc in range(1, T+1):
    # n : 원소의 개수
    # m : 구간의 길이
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    max_v = 0
    min_v = 987654321

    # 중복된 연산을 피하자....
    # 첫구간은 구해놓자..
    tmp = 0
    for i in range(m):
        tmp += nums[i]

    for i in range(m, n):
        # 중복되는 가운데 구간 + 새로운 요소 1개 - 기존의 1번째 요소
        tmp = tmp + nums[i] - nums[i - m]


    print('#{} {}'.format(tc, max_v - min_v))