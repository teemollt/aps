import sys
sys.stdin = open("sample_input (binsearch).txt")

def bin_search(arr, l, r, check):
    if l > r:
        return 0
    else:
        m = (l+r)//2
        if target == arr[m]:
            return 1
        elif target < arr[m]:
            # print('left')
            if not check or check[-1] == 'right':
                check.append('left')
                return bin_search(arr, l, m-1, check)
            else:
                return 0
        else:
            # print('right')
            if not check or check[-1] == 'left':
                check.append('right')
                return bin_search(arr, m+1, r, check)
            else:
                return 0



t = int(input())
for tc in range(1, t+1):
    # a와 b에 속한 정수의 개수 n,m
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    cnt = 0
    # print(a, b)
    for i in range(m):
        target = b[i]
        check = []
        if bin_search(a, 0, n-1, check):
            cnt += 1
    print('#{} {}'.format(tc, cnt))