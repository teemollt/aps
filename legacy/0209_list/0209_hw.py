import sys
sys.stdin = open("input (1208).txt")
T = 10
for tc in range(1, T+1):
    # 입력
    dump = int(input())
    boxes = list(map(int, input().split()))
    # max_idx = 0
    # min_idx = 0
    # 덤프 가능한 횟수만큼 최고높이 박스 -1 최저높이 박스 +1 반복
    max_idx = 0
    min_idx = 0
    for i in range(dump):
        # 최고높이
        max_h = boxes[0]

        # 최저높이
        min_h = boxes[0]


        # 최고 최저 찾기 박스 개수만큼 반복
        for j in range(len(boxes)):
            if max_h <= boxes[j]:
                max_h = boxes[j]
                max_idx = j

            if min_h >= boxes[j]:
                min_h = boxes[j]
                min_idx = j

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # 마지막 덤프가 일어난 이후 다시 최고층 최저층 idx 찾아서 빼줘야함.

        for j in range(len(boxes)):
            if max_h <= boxes[j]:
                max_h = boxes[j]
                max_idx = j
            if min_h >= boxes[j]:
                min_h = boxes[j]
                min_idx = j

    rst = boxes[max_idx] - boxes[min_idx]

    print('#{} {}'.format(tc, rst))
