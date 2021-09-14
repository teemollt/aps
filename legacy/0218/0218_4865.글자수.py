import sys
sys.stdin = open("sample_input (3).txt")

t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)

    di = {}
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        di[i] = cnt

    max_v = 0
    for i in di.values():
        if max_v <= i:
            max_v = i

    print('#{} {}'.format(tc, max_v))