import sys
sys.stdin = open("input.txt")
# for k in range(1, 11):
#     t = int(input())
#     bds = list(map(int, input().split()))
#     rst = 0
#     for i in range(2, len(bds) - 2):
#         if bds[i-2] < bds[i] and bds[i-1] < bds[i] and bds[i+2] < bds[i] and bds[i+1] < bds[i]:
#             bd2 = []
#             bd2.append(bds[i - 1])
#             bd2.append(bds[i + 1])
#             bd2.append(bds[i + 2])
#             fbd2 = bds[i - 2]
#             for j in bd2:
#                 if fbd2 < j:
#                     fbd2 = j
#             rst += (bds[i] - fbd2)
#
#     print(f'#{k} {rst}')

T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    # 입력 완료
    # 1. 반복문을 돌면서 각 빌딩의 조망권 계산
    # 2. 조망권 계산은 현재 요소의
    # 현재요소위치 -1, -2, +1, +2에 위치한 건물들중에 가장높은 건물의 높이를 구함
    # 3. 인접한 건물들중에 가장높은 높이가 현재 건물의 높이보다 작으면
    # 현재건물 높이 - 인접건물 최고 높이 = 조망권 확보된 세대수
    # 1. 반복문
    rst = 0
    for i in range(2,N-2):
        # 현재건물의 높이 buildings[i]
        # 양쪽거리 2 안에 있는 건물들 중에 가장 높은 건물의 높이 찾기
        tmp = list()
        tmp.append(buildings[i-2])
        tmp.append(buildings[i-1])
        tmp.append(buildings[i+2])
        tmp.append(buildings[i+1])
        # 건물의 높이가 가장 큰 인접건물 찾기
        # 최대값 찾기, 최대값 저장을 위한 변수 선언 --> 최대한 작은 값 or 비교대상 중 하나(0 index라든가..)
        max_v = tmp[0]
        for j in range(len(tmp)):
            if tmp[j] > max_v:
                max_v = tmp[j]
        # 반복문 완료 후에 max_v에는 인접건물의 최대값 저장되어 있음.
        # 조망권 확보 세대 구하기
        if max_v < buildings[i]:
            rst += buildings[i] - max_v

    print("#{} {}".format(tc, rst))
