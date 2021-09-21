import sys
input = sys.stdin.readline
n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]
t.sort(key=lambda x: (x[1], x[0]))
cnt, e = 0, 0
for i in range(n):
    if e <= t[i][0]:
        cnt += 1
        e = t[i][1]
print(cnt)