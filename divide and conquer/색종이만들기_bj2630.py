
def sol(n, arr, x, y):
    global white
    global blue
    # 색종이를 더이상 나눌수 없는 경우 그냥 카운트
    if n == 1:
        if arr[y][x]:
            blue += 1
        else:
            white += 1
        return
    m = n // 2
    c = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if c != arr[i][j]:
                # 4등분 재귀
                sol(m, arr, x, y)
                sol(m, arr, x+m, y)
                sol(m, arr, x, y+m)
                sol(m, arr, x+m, y+m)
                return
    else:
        if arr[y][x]:
            blue += 1
        else:
            white += 1

# 한변의 길이 n
n = int(input())
# 색종이
arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
sol(n, arr, 0, 0)
print(white)
print(blue)
