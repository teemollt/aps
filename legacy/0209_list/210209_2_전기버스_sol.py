import sys
sys.stdin = open("sample_input (1).txt")
# T = int(input())
#
# for tc in range(1, T+1):
#     # k : 한번 충전으로 이동할 수 있는 거리
#     # n : 마지막 종점의 위치
#     # m : 충전소의 개수
#     k, n, m = map(int, input().split())
#     charge = list(map(int, input().split()))
#     bus_stop = [0] * (n+1)
#
#     # for i in range(m):
#     #     bus_stop[charge[i]] = 1
#     for i in charge:
#         bus_stop[i] = 1
#
#     bus = 0 # 버스위치
#     ans = 0 # 충전횟수
#
#     while True:
#         # 버스가 이동할 수 있는만큼 이동하자.
#         bus += k
#         # 종점에 도착하거나 종점을 지나 더 나간 경우 종료
#         if bus >= n:
#             break
#         for i in range(bus, bus - k, -1):
#             if bus_stop[i]:
#                 ans += 1
#                 bus = i
#                 break
#         # 충전기를 못찾았을때
#         else:
#             ans = 0
#             break
#
#     print('#{} {}'.format(tc, ans))

    #################################풀이 2#######################

T = int(input())

for tc in range(1, T + 1):
     # k : 한번 충전으로 이동할 수 있는 거리
    # n : 마지막 종점의 위치
    # m : 충전소의 개수
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    ans = 0

    #
    charge = [0] + charge + [n]
    # charge.insert(0, 0)
    # charge.append(n)

    last = 0
    # 충전소 개수에다가 출발점과 도착지를 넣어놨으므로 m+2
    for i in range(1, m+2):
        if charge[i] - charge[i-1] > k:
            ans = 0
            break
        # 갈 수 있으면 아무작업 X
        # 갈 수 없다면 내 바로 직전 충전소로 위치를 옮기고 횟수 1회증가
        if charge[i] > last + k:
            last = charge[i-1]
            ans += 1


    print('#{} {}'.format(tc, ans))