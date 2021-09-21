import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
used, rst, v =[0] * n, 1e9, 0
s, l = [0]*(n//2), [0]*(n//2)
def sol(idx, d):
    global rst
    if d == n/2:
        sv, lv = 0, 0
        for i in range(n//2):
            for j in range(n//2):
                if i != j:
                    sv += arr[s[i]][s[j]]
                    lv += arr[l[i]][l[j]]
        if abs(sv-lv) < rst:
            rst = abs(sv-lv)
        return
    for i in range(idx, n):
        if not used[i]:
            used[i] = 1
            s[d] = i
            for j in range(n):
                if not used[j]:
                    used[j] = 1
                    l[d] = j
                    sol(i+1, d+1)
                    used[j] = 0
                    l[d] = 0
            used[i] = 0
            s[d] = 0
sol(0, 0)
print(rst)
