# import sys
# sys.stdin = open("sample_input (이진수2).txt")

def sol(num, d):
    global rst
    # 13자리 넘어가면 overflow 출력
    if d > 13:
        rst = 'overflow'
        return
    if num < 0.00000000000000000001:
        return
    st = 2 ** (-1 * d)
    # 자리수 -1부터 확인해서 크면 1 작으면 0 넣기
    if float(num) >= st:
        rst += '1'
        sol(num-st, d+1)
    else:
        rst += '0'
        sol(num, d + 1)


t = int(input())
for tc in range(1, t+1):
    n = input()
    rst = ''
    sol(float(n), 1)
    print('#{} {}'.format(tc, rst))