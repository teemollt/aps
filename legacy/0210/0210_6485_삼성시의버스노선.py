import sys
sys.stdin = open("s_input.txt")
t = int(input())
for tc in range(1, t+1):
    # 입력
    # n : 버스 노선 개수
    # i 번째 버스노선 -> Ai ~ Bi 정류장
    # p : 버스 정류장 개수
    # 각 버스 정류장엔 1~p 정류장번호 붙어있고 각각 몇개의 버스 노선이 다니는지
    # 버스 정류장 번호를 idx로 가지는 배열 만들어 놓고 버스가 지나갈때마다 +1
    n = int(input())
    stop = [0] * 5001
    for i in range(1, n+1):
        # 1번버스부터 정류장 범위 입력
        bus = list(map(int, input().split()))
        # bus에는 i번 버스의 정류장 범위가 입력되어있음 ex) [1, 5] => 1~5번 정류장
        # 정류장을 하나씩 지나가면서 stop의 해당 idx에 +1
        for j in range(bus[0], bus[1]+1):
            stop[j] += 1
    # 정류장 개수 p를 받고
    p = int(input())
    # p까지만 반복해서 rst에 추가
    print('#{}'.format(tc), end=' ')
    rst = []
    for i in range(1, p+1):
        idx = int(input())
        print(stop[idx], end=' ')
    print()
