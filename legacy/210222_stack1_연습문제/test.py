# 추억의 2048게임
# import sys
#
# sys.stdin = open("input.txt", "r")
T = int(input())
for t in range(1, T+1):
    N, direct = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    # 먼저 합치고, 빈칸 채우기
    if direct == "up":
        # 세로 끼리 합치기
        for i in range(N):
            for j in range(N-1):
                for k in range(j+1, N):
                    if board[k][i] != 0:
                        if board[j][i] == board[k][i]:
                            board[j][i] = board[j][i] * 2
                            board[k][i] = 0
                        break
        # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
        for i in range(N):
            for j in range(N-1):
                if board[j][i] == 0:
                    for k in range(j+1, N):
                        if board[k][i] != 0:
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            break
    elif direct == "right":
        # 오른쪽으로 밀기
        for i in range(N):
            for j in range(N - 1, 0, -1):
                for k in range(j-1, -1, -1):
                    if board[i][k] != 0:
                        if board[i][j] == board[i][k]:
                            board[i][j] = board[i][j] * 2
                            board[i][k] = 0
                        break
        # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if board[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        if board[i][k] != 0:
                            board[i][j] = board[i][k]
                            board[i][k] = 0
                            break

    elif direct == "down":
        # 세로 끼리 합치기
        for i in range(N):
            for j in range(N - 1, 0, -1):
                for k in range(j - 1, -1, -1):
                    if board[k][i] != 0:
                        if board[j][i] == board[k][i]:
                            board[j][i] = board[j][i] * 2
                            board[k][i] = 0
                        break
        # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if board[j][i] == 0:
                    for k in range(j - 1, -1, -1):
                        if board[k][i] != 0:
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            break
    elif direct == "left":
        # 왼쪽으로 밀기
        for i in range(N):
            for j in range(N - 1):
                for k in range(j + 1, N):
                    if board[i][k] != 0:
                        if board[i][j] == board[i][k]:
                            board[i][j] = board[i][j] * 2
                            board[i][k] = 0
                        break
        # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
        for i in range(N):
            for j in range(N - 1):
                if board[i][j] == 0:
                    for k in range(j + 1, N):
                        if board[i][k] != 0:
                            board[i][j] = board[i][k]
                            board[i][k] = 0
                            break
    print("#%d" % t )
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
