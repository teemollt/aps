import sys
sys.stdin = open("sample_input (1).txt")

t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)
    rst = 0
    for i in range(m-n+1):
        if str1[:] == str2[i:i+n]:
            rst = 1

    print('#{} {}'.format(tc, rst))