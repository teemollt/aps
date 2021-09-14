import sys
sys.stdin = open('sample_input (최소합).txt')

def sol(x, y, sum):
    global rst
    global min_v
    sum += arr[y][x]
    # 끝까지 안가더라도 이미 합이 min_v보다 커질 경우에 종료해버림
    # 이거 하기 전에는 시간초과 났었음...
    if sum > min_v:
        return
    if x == y == n-1:
        # rst.append(sum)
        # return
        if sum < min_v:
            min_v = sum
        return
    if 0 <= x < n-1 and 0 <= y < n-1:
        for i in range(2):
            sol(x+dx[i], y+dy[i], sum)
    elif x < n and y < n-1:
        sol(x+dx[1], y+dy[1], sum)
    elif x < n-1 and y < n:
        sol(x + dx[0], y + dy[0], sum)
# bfs가 더 오래걸림...
# def sol(x, y, sum):
#     global min_v
#     q = []
#     p = (x, y, arr[y][x])
#     q.append(p)
#     while q:
#         cx, cy, sum = q.pop(0)
#         if 0 <= cx < n-1 and 0 <= cy < n-1:
#             for i in range(2):
#                 nx = cx+dx[i]
#                 ny = cy+dy[i]
#                 q.append((nx, ny, sum+arr[ny][nx]))
#         elif cx < n and cy < n-1:
#             nx = cx+dx[1]
#             ny = cy+dy[1]
#             q.append((nx,ny,sum+arr[ny][nx]))
#         elif cx < n-1 and cy < n:
#             nx = cx+dx[0]
#             ny = cy+dy[0]
#             q.append((nx, ny, sum + arr[ny][nx]))
#         if cx == cy == n-1:
#             if sum < min_v:
#                 min_v = sum
#     return
t = int(input())
for tc in range(1, t+1):
    # 가로세로 줄수 n
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 오른쪽, 아래
    dx = [1, 0]
    dy = [0, 1]
    min_v = 987654321
    sol(0,0,0)
    print('#{} {}'.format(tc, min_v))