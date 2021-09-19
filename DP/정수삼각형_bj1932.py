from sys import stdin
input = stdin.readline
n = int(input())
t = []
rst = 0
for i in range(n):
    t.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(t[i])):
        if j == 0:
            t[i][j] = t[i][j] + t[i-1][j]
        elif j < len(t[i])-1:
            t[i][j] = max(t[i][j] + t[i-1][j], t[i][j] + t[i-1][j-1])
        else:
            t[i][j] = t[i][j] + t[i-1][j-1]
print(max(t[n-1]))


