import sys
sys.stdin = open("s_input.txt")
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = [0] * 5001

    for i in range(n):
        a, b = map(int, input().split())

        # 해당 정류장에 지나는 버스 대수 누적
        for j in range(a, b+1):
            stop[j] += 1

    p = int(input())

    print('#{}'.format(tc), end=' ')
    for i in range(p):
        # 우리가 확인하고 싶은 정류장의 번호
        c = int(input())
        print(stop[c], end=' ')
    print()