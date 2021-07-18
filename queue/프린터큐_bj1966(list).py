from sys import stdin
t = int(stdin.readline())
for tc in range(t):
    # n 문서개수, m 궁금한 문서가 몇번째 있는지
    n, m = map(int, stdin.readline().split())
    pri = list(map(int, stdin.readline().split()))
    for i in range(n):
        pri[i] = (pri[i], i)
    od = 1
    while pri:
        if pri[0][0] == max(pri)[0]:
            if pri[0][1] == m:
                print(od)
                break
            pri.pop(0)
            od += 1
        else:
            pri.append(pri.pop(0))

