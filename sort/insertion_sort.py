# insertion_sort

def insertion_sort(arr):
    # 두번째 요소부터 시작해서 끝까지
    for i in range(1, len(arr)):
        # 이미 정렬된 부분 거꾸로 순회 하면서 위치 찾기
        for j in range(i, 0, -1):
            # 위치 하나씩 바꿔가면서 확인 i번째 요소보다 작은값이 나오면 바로 이전 위치에 삽입
            # j-1이 더크면
            if arr[j] < arr[j-1]:
                # 위치 바꾸기
                arr[j], arr[j-1] = arr[j-1], arr[j]
            # 작은값이 나오면 멈추기
            else:
                break
    return arr
arr = [4,5,2,3,4,5,2,4,6,6,88,2,4,3,6,1,41,23,10]
print(insertion_sort(arr))