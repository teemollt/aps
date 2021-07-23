def sol(n, x, y):
    global a, b, c
    if n == 1:
        if arr[y][x] == -1:
            a += 1
        elif arr[y][x] == 0:
            b += 1
        elif arr[y][x] == 1:
            c += 1
        return
    m = n // 3
    s = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if s != arr[i][j]:
                sol(m, x, y)
                sol(m, x+m, y)
                sol(m, x+2*m, y)
                sol(m, x, y+m)
                sol(m, x+m, y+m)
                sol(m, x+2*m, y+m)
                sol(m, x, y+2*m)
                sol(m, x+m, y+2*m)
                sol(m, x+2*m, y+2*m)
                return
    else:
        if s == -1:
            a += 1
        elif s == 0:
            b += 1
        elif s == 1:
            c += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
a, b, c, = 0, 0, 0
sol(n, 0, 0)
print(a)
print(b)
print(c)
