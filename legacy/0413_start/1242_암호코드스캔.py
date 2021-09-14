import sys
sys.stdin = open("sample_input (1242).txt")
def hex_to_binary(n):
    # 10진수로
    if ord('0') <= ord(n) <= ord('9'):
        num = int(n)
    else:
        num = ord(n) - ord('A') + 10
    # 2진수로
    binary = ''
    for i in range(4):
        binary = str(num % 2) + binary
        num //= 2
    return binary

# 유효성 검사
def valid(v):
    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            # 홀수번째 합
            odd += v[i]
        else:
            even += v[i]
    if (odd * 3 + even) % 10 == 0:
        return odd + even
    return 0

code = {(3,2,1,1): 0, (2,2,2,1): 1, (2,1,2,2): 2, (1,4,1,1): 3, (1,1,3,2): 4, (1,2,3,1): 5, (1,1,1,4):6,
        (1,3,1,2): 7, (1,2,1,3): 8, (3,1,1,2): 9}

t = int(input())
for tc in range(1, t+1):
    #세로 N 가로 M
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # arr을 전부 2진수로 바꿔버려
    for i in range(N):
        bin = ''
        for j in range(M):
            bin += hex_to_binary(arr[i][j])
        arr[i] = bin

    cnt = 0
    used = []
    for i in range(N):
        idx = M*4
        # 뒤쪽부터 검사, 전부 2진수로 만들었으니 전체길이 * 4
        for j in range(M*4-1, -1, -1):
            if j >= idx:
                continue
            # 1 나오면 거기부터 시작
            if arr[i][j] == '1':
                idx = j
                decode = []
                for k in range(8):
                    n1 = n2 = n3 = n4 = 0
                    while arr[i][idx] == '1':
                        n4 += 1
                        idx -= 1
                    while arr[i][idx] == '0':
                        n3 += 1
                        idx -= 1
                    while arr[i][idx] == '1':
                        n2 += 1
                        idx -= 1
                    # n2~4 중에 가장 작은게 굵기 * 1
                    w = min(n2, n3, n4)
                    n1 = 7*w - n2 - n3 - n4
                    idx -= n1
                    # decode에 변환된 숫자 삽입
                    decode.insert(0, code[(n1//w, n2//w, n3//w, n4//w)])
                # 중복확인
                if decode not in used:
                    used.append(decode)
                    cnt += valid(decode)

    print('#{} {}'.format(tc, cnt))


