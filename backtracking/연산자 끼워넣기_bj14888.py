import sys
input = sys.stdin.readline
n = int(input())
# 주어지는 숫자
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
INF = 1e9
maxv, minv = -INF, INF
def bt(d, rst, ad, su, mu, di):
    global maxv, minv
    if d == n:
        if rst > maxv:
            maxv = rst
        if rst < minv:
            minv = rst
        return
    if ad:
        bt(d+1, rst+nums[d], ad-1, su, mu, di)
    if su:
        bt(d+1, rst-nums[d], ad, su-1, mu, di)
    if mu:
        bt(d+1, rst*nums[d], ad, su, mu-1, di)
    if di:
        if rst >= 0:
            bt(d + 1, rst//nums[d], ad, su, mu, di-1)
        else:
            bt(d + 1, -(-rst//nums[d]), ad, su, mu, di-1)
bt(1, nums[0], op[0], op[1], op[2], op[3])
print(maxv)
print(minv)