import sys
sys.stdin = open("input (1208).txt")
# # 최저 높이 상자 인덱스 위치 반환
# def min_search():
#     min_v = 987654321
#     min_idx = -1
#
#     for i in range(len(box)):
#         if box[i] < min_v:
#             min_v = box[i]
#             min_idx = i
#
#     return min_idx
#
# def max_search():
#     max_v = 0
#     max_idx = -1
#
#     for i in range(len(box)):
#         if max_v < box[i]:
#             max_v = box[i]
#             max_idx = i
#
#     return max_idx
#
#
# T = 10
# for tc in range(1, T+1):
#     # 입력
#     n = int(input())
#     box = list(map(int, input().split()))
#     max_idx = 0
#     min_idx = 0
#
#     # n번 덤프하기
#     for i in range(n):
#         # 최고 높이 상자 한칸 내리기
#         box[max_search()] -= 1
#         # 최저 높이 상자 한칸 올리기
#         box[min_search()] += 1
#
#     print('#{} {}'.format(tc, box[max_search()] - box[min_search()]))
#
# ##########################풀이2##################정렬활용#######################풀이2########################
# def bubble_sort(arr):
#     for i in range(len(arr)-1, 0, -1):
#         for j in range(0, i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# T = 10
# for tc in range(1, T+1):
#     # 입력
#     n = int(input())
#     box = list(map(int, input().split()))
#
#     for i in range(n):
#         bubble_sort(box)
#         box[0] += 1
#         box[-1] -= 1
#
#     bubble_sort(box)
#
#     print('#{} {}'.format(tc, box[-1] - box[0]))

######################풀이3#####################인덱스 활용##########################풀이3#########################
# 박스의 개수(높이)가 최대 100이므로 높이는 0~100까지 나올수 있음. --> 0~100 인덱스를 가지는 배열을 만들어
# idx = 높이 , value = 해당 높이를 가진 box 개수
# 이렇게 되면 idx가 가장 큰 value -1 가장 작은 value +1 해나가면 됨.
T = 10
for tc in range(1, T+1):
    # 입력
    n = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101

    # 초기화
    min_v = 100
    max_v = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자.
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_v:
            max_v = box[i]
        if box[i] < min_v:
            min_v = box[i]

    while n > 0 and min_v < max_v - 1:
        # 상자 옮기기
        h_cnt[min_v] -= 1
        h_cnt[min_v+1] += 1

        h_cnt[max_v] -= 1
        h_cnt[max_v-1] += 1

        # 포인터를 변경
        if h_cnt[min_v] == 0:
            min_v += 1

        if h_cnt[max_v] == 0:
            max_v -= 1

        # 덤프 줄이기
        n -= 1

    print('#{} {}'.format(tc, max_v - min_v))