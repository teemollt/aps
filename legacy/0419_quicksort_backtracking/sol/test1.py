import sys
sys.stdin = open("sample_input (binsearch).txt")
def binarySearch(a, key):
    global result
    result = []
    start = 0
    end = len(a)-1
    if key not in a:
        return []
    while start<=end:
        mid = start+(end-start)//2
        if key == a[mid]:   #조건을 만족하면서 key 값을 찾은경우...
            return result
        elif key < a[mid]:
            end = mid - 1
            # result += '0'
            result.append('left')
        else:
            start = mid + 1
            # result += '1'
            result.append('right')
    return result

T = int(input())

for tc in range(1, T+1):
# for tc in range(1, 3):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 찾고자 하는 값이 m보다 컸다가 작았다가 or 작았다가 크거나
    # 찾고자 하는 값이 m이 되는 경우는 고려하지 않는다.
    # 1번 tc의 경우는 2, 3이 포함되나?

    print('#{}'.format(tc))
    for i in range(len(B)):
        print(binarySearch(A, B[i]))
    print('*')
