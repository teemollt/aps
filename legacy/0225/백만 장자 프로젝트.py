import sys
sys.stdin = open('input (mil).txt')
t = int(input())
for tc in range(1, t+1):
    N = int(input())
    price = list(map(int, input().split()))
    # 뒤에서부터 가격을 검사해서 더 큰게 나오기전까지 차이를 계속 더해나간다..
    max_v = 0
    rst = 0
    for i in range(N-1, -1, -1):
        if max_v < price[i]:
            max_v = price[i]
        else:
            rst += max_v - price[i]

    print('#{} {}'.format(tc, rst))