# import sys
# sys.stdin = open("sample_input (이진수).txt")

def hex_to_binary(n):
    # 10진수로
    if ord('0') <= ord(n) <= ord('9'):
        num = int(n)
    else:
        num = ord(n) - ord('A') + 10
    # 2진수로
    binary = [0] * 4
    for i in range(3, -1, -1):
        binary[i] = str(num % 2)
        num //= 2
    return binary

t = int(input())
for tc in range(1, t+1):
    N, number = map(str, input().split())
    N = int(N)
    # print(N)
    # print(number)
    rst = ''
    for i in range(N):
        rst += ''.join(hex_to_binary(number[i]))
    print('#{} {}'.format(tc, rst))

