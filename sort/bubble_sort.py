# bubble sort

def bubble_sort(arr):
    # 배열 전체 뒤에서부터 하나씩
    for i in range(len(arr)-1, -1, -1):
        # 바로 다음 요소랑 비교해서 더크면 자리 바꾸기
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input())
arr = list(map(int, input().split()))
print(bubble_sort(arr))
