# 첫째 줄에는 영상의 크기를 나타내는 숫자 N  N 은 언제나 2의 제곱수
# 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있음
import sys

def sol(n, x, y):
    global rst
    # 더이상 쪼갤수 없다면
    if n == 1:
        if arr[y][x]:
            rst += "1"
        else:
            rst += "0"
        return
    m = n // 2
    # 범위 전체탐색하면서 다른게 있나 확인
    s = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            # 탐색하다가 다른게 하나라도 나오면 사등분
            if s != arr[i][j]:
                rst += "("
                sol(m, x, y)
                sol(m, x+m, y)
                sol(m, x, y+m)
                sol(m, x+m, y+m)
                rst += ")"
                return
    # 멈추지 않고 다 돌았다면
    else:
        if s:
            rst += "1"
        else:
            rst += "0"

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
rst = ""
sol(n, 0, 0)
print(rst)