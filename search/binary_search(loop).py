# while문으로 이진탐색
def search(arr, target, s, e):
    # 시작점이 끝점보다 커지면 안됨
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            return mid
        #
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1

arr = [2,4,6,9,12,15,17,23,27,32,37,39,40,50]
target = 12
print(search(arr, target, 0, len(arr)))