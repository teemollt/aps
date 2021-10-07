import sys
input = sys.stdin.readline
def sol():
    n = int(input())
    m = list(map(int, input().split()))
    arr = [1]*n
    arr2 = [1]*n
    for i in range(1, n):
        for j in range(i):
            if m[i]>m[j]:
                arr[i] = max(arr[i], arr[j]+1)
            if m[i]<m[j]:
                arr2[i] = max(arr2[i], arr[j]+1, arr2[j]+1)
    print(max(max(arr), max(arr2)))
sol()