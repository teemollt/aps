import sys
sys.stdin = open("input (2).txt")
t = int(input())
for tc in range(1, t+1):
    # 입력
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    v_list = []
    total = 0
    # n이 클때, m이 클때 나눠서..
    if n < m:
        for i in range(m-n+1):
            v = 0
            for j in range(n):
                v += (a[j] * b[i+j])
            v_list.append(v)
    else:
        for i in range(n-m+1):
            v = 0
            for j in range(m):
                v += (a[i+j] * b[j])
            v_list.append(v)

    # 결과값 리스트에서 제일 큰수 찾기
    rst = v_list[0]
    for i in v_list:
        if rst <= i:
            rst = i

    print('#{} {}'.format(tc, rst))
