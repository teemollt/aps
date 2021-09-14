import sys
sys.stdin = open("sample_input (3).txt")
def search(key):
    cnt = 0
    l, r = 1, p
    while l <= r:
        c = (l+r) // 2
        cnt += 1
        if c == key:
            return cnt
        elif c < key:
            l = c
        else:
            r = c


t = int(input())
for tc in range(1, t+1):
    p, a, b = map(int, input().split())
    print('#{}'.format(tc), end=" ")
    if search(a) < search(b):
        print("A")
    elif search(a) > search(b):
        print("B")
    else:
        print(0)