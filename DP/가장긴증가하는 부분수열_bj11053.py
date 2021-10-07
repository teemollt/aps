import sys
input = sys.stdin.readline
def sol():
    n = int(input())
    a = list(map(int, input().split()))
    arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            # 현재값a[i] 이전을 a[j]로전부 돌면서
            # a[i]보다 a[j] 작은 경우엔 돌면서 갱신중인 arr[i]와 arr[j] 매번 비교해서 큰값을 남김
            # a[i]보다 a[j]가 작은 경우의 arr 값 중 가장큰값 +1이 최종적으로 arr[i]에 남게됨
            if a[i] > a[j]:
                arr[i] = max(arr[j] + 1, arr[i])
    print(max(arr))
sol()
