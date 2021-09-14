arr = [6,5,2,3,1]

def sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)

sort(arr)

# A : 대상배열
# i : 몇번째 요소를 정렬할지 결정하는 변수
# N : 요소 개수
def selection_sort(arr, i, N):

    if i == N:
        print(arr)
        return

    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
    selection_sort(arr, i+1, N)

selection_sort(arr, 0, 5)