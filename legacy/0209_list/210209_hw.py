T = 1
for tc in range(1, T+1):
    # 입력
    dump = 2
    boxes = [5, 8, 3, 1, 5, 6, 9, 9, 2, 2, 4]
    max_idx = 0
    min_idx = 0
    # 덤프 가능한 횟수만큼 최고높이 박스 -1 최저높이 박스 +1 반복
    for i in range(dump):
        # 최고높이
        max_h = boxes[0]

        # 최저높이
        min_h = boxes[0]

        # 최고 최저 찾기 박스 개수만큼 반복해서
        for j in range(len(boxes)):
            if max_h <= boxes[j]:
                max_h = boxes[j]
                max_idx = j
            if min_h >= boxes[j]:
                min_h = boxes[j]
                min_idx = j


        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        for j in range(len(boxes)):
            if max_h <= boxes[j]:
                max_h = boxes[j]
                max_idx = j
            if min_h >= boxes[j]:
                min_h = boxes[j]
                min_idx = j

    rst = boxes[max_idx] - boxes[min_idx]

    print('#{} {}'.format(tc, rst))
