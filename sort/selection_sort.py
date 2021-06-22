# selection sort

def selection_sort(arr):
    # 전체 리스트 돌면서
    for i in range(len(arr)):
        # 한사이클마다 최솟값과 그 위치 찾기 위해 min_idx 초기화
        min_idx = i
        # 이미 i-1은 최솟값으로 결정됐으므로
        # i 부터 끝까지 돌면서 최솟값 찾기
        for j in range(i, len((arr))):
            # j자리의 값이 min_idx자리의 값보다 작으면
            if arr[j] < arr[min_idx]:
                # min_idx 교체
                min_idx = j
        # i자리와 최솟값 자리 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [3,4,6,2,6,87,4,3,5,7,2,24,10,16,10]
print(selection_sort(arr))