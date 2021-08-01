# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
import sys
def bs(arr, x):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            l = mid+1
        else:
            r = mid-1
    else:
        return 0

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
arr.sort()
for i in range(m):
    print(bs(arr, x_list[i]))

