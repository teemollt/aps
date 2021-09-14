import sys
sys.stdin = open("sample_input (quick).txt")

# 함수 하나 더쓰면 시간초과남..
# def partition(arr, l, r):
#     pivot = arr[l]
#     # i = l
#     # j = r
#     # while i <= j:
#     #     while i <= j and arr[i] <= pivot:
#     #         i += 1
#     #     while arr[j] > pivot:
#     #         j -= 1
#     #     if i < j:
#     #         arr[i], arr[j] = arr[j], arr[i]
#     # arr[l], arr[j] = arr[j], arr[l]
#     # return j
#     i = l
#     for j in range(l+1, r+1):
#         if arr[j] < pivot:
#             i += 1
#             arr[j], arr[i] = arr[i], arr[j]
#     arr[l], arr[i] = arr[i], arr[l]
#     return i

def quick_sort(arr, l, r):
    if r > l:
        pivot = arr[l]
        i = l
        j = r
        while i <= j:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i<=j and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[j] = arr[j], arr[l]
        pivot = j
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, n-1)
    print('#{} {}'.format(tc, arr[n//2]))
    print(arr)
