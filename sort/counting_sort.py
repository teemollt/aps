# counting_sort

def counting_sort(arr):
    idx_list = [0] * (max(arr) + 1)
    arr2 = []
    for i in arr:
        idx_list[i] += 1
    for n in range(len(idx_list)):
        for _ in range(idx_list[n]):
            arr2.append(n)
    return arr2


arr = [4,5,6,2,5,6,7,3,13,52,10]
print(counting_sort(arr))