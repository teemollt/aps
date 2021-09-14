import sys
sys.stdin = open("sample_input (1).txt")
T = int(input())
for tc in range(1, T+1):
    # 입력 받기(k 1충전시 최대이동 정류장수, n 종점 정류장, m 충전기 설치된 정류장 개수)
    k, n, m = map(int, input().split())
    # 충전기가 설치된 정류장 번호 입력
    num = list(map(int, input().split()))
    # 반복문으로 버스 이동
    # 마지막 버스 충전 위치
    bus_charge = 0
    # 현재 버스 위치
    bus = 0
    # 충전기 이용횟수
    charge = 0
    # 충전기 이용가능 위치??
    possible = []
    # 마지막 충전위치로 부터 갈수있는 거리인 k만큼 갔을때 종점인 n보다 커진다면 stop 그전까지 반복
    while bus_charge + k < n:
        # 1칸 이동시 마다 버스 1칸 이동
        bus += 1
        # 버스 이동위치에 충전소가 있으면 이용가능 위치 목록에 추가
        if bus in num:
            possible.append(bus)
        # 이동위치가 1충전시 갈수있는 최대값에 다다르면 충전소 이용가능 위치 목록중 제일 큰값 찾기
        # 마지막 버스충전 위치 + k --> 버스가 1번 충전하고 갈수있는 최대거리에 버스가 도착했을 경우
        # 그동안 쌓아놨던 그 사이에 있는 충전 가능 장소 중 가장 큰 값을 찾아서
        # 마지막 버스 충전 장소로 저장하고 거기서 부터 다시 버스 출발하는 것으로 설정
        if bus_charge + k == bus:
            if possible == []:
                charge = 0
                break
            else:
                max_v = possible[0]
                for j in possible:
                    if max_v < j:
                        max_v = j
            # 제일 큰값에서 충전했으면 그 값이 버스 위치 / 마지막 충전위치 and 충전횟수 +1 / 충전가능위치 초기화
            bus = max_v
            bus_charge = max_v
            charge += 1
            possible = []

    print('#{} {}'.format(tc, charge))