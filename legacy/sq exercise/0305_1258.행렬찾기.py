import sys
sys.stdin = open("input (1258).txt")
# 부분 행렬들을 개수와 그 뒤를 이어 행렬들의 행과 열의 크기를 출력한다.
# 크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력한다.

# 0,0 부터 검사 시작해서 0이 아닌 숫자가 나오면 거기서부터 오른쪽, 아래쪽으로만 검사시작
# 검사해서 0이 나오는 순간 각각 가로 세로 길이를 반환하고 그 사각형 전체를 방문처리 -> 0으로 변환
# 위 과정 반복.
def sol(y, x):
    global arr
    # 아래로, 오른쪽으로
    # 0이 나올때까지 두 방향 따로하자 길이가 다를수 있으니까
    iy, ix = 0, 0
    sg = [0]*3
    # 오른쪽 탐색 0이 아니거나 행렬 끝이거나
    while arr[y][x+ix] and x+ix < n:
        ix += 1
    # 반복문이 끝나고 ix만큼 오른쪽으로 이동 가능했으므로 이게 부분사각형의 가로 길이
    sg[1] = ix
    while arr[y+iy][x] and y+iy < n:
        iy += 1
    sg[0] = iy
    # 방문한 사각형 전부 0처리하고 y ~ y+iy
    for i in range(y, y+iy+1):
        for j in range(x, x+ix+1):
            arr[i][j] = 0
    sg[2] = ix * iy
    return sg

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 검사 시작점 탐색
    rst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                rst.append(sol(i, j))
    # 부분사각형 크기 비교
    for i in range(len(rst)):
        min = i
        for j in range(i+1, len(rst)):
            if rst[j][2] < rst[min][2]:
                min = j
        rst[i], rst[min] = rst[min], rst[i]

    for i in range(len(rst)-1):
        for j in range(len(rst)-i-1):
            if rst[j+1][2] == rst[j][2]:
                if rst[j+1][0] < rst[j][0]:
                    rst[j+1], rst[j] = rst[j], rst[j+1]

    print('#{} {}'.format(tc, len(rst)), end=" ")
    for i in range(len(rst)):
        print('{} {}'.format(rst[i][0], rst[i][1]), end=" ")
    print()
