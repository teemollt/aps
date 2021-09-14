import sys
sys.stdin = open("sample_input(o).txt")

def dol(a, b, c):
    arr[b][a] = c
    pass


t = int(input())
for tc in range(1, t+1):
    # 한변의 길이 n (4, 6, 8), 돌놓는 횟수 m
    n, m = map(int, input().split())
    arr = [[0]*(n+2) for _ in range(n+2)]
    # 기본 돌 깔기
    arr[n//2][n//2] = 2
    arr[n//2+1][n//2] = 1
    arr[n//2][n//2+1] = 1
    arr[n//2+1][n//2+1] = 2
    # 검사 방향 설정 리스트 12시부터 시계방향
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    # 돌위치 입력 ex) 1흑돌, 2 백돌 3 2 1 (3, 2) 흑돌
    for i in range(m):
        x, y, color = map(int, input().split())
        arr[y][x] = color
        # 돌이 놓인곳기준 12시방향부터 8방향 검사
        for q in range(8):
            # 다른 색 돌이 떴을때 idx를 저장할 스택
            stack_x = []
            stack_y = []
            num = 1
            # 같은 색이나올때까지 반복
            while arr[y+dy[q]*num][x+dx[q]*num] != arr[y][x]:
                # 방금 놓은 돌과 다른 색이면 위치 저장
                if arr[y][x] != arr[y+dy[q]*num][x+dx[q]*num]:
                    stack_y.append(y+dy[q]*num)
                    stack_x.append(x+dx[q]*num)
                # 같은색 안나오고 0나오면 스택 비우고 break
                if arr[y+dy[q]*num][x+dx[q]*num] == 0:
                    stack_x = []
                    stack_y = []
                    break
                num += 1


            # 위과정 완료후 스택이 빌때까지 색 바꿔주기
            while stack_x:
                arr[stack_y.pop()][stack_x.pop()] = arr[y][x]

        cnt1 = 0
        cnt2 = 0
        for i in range(n+2):
            for j in range(n+2):
                if arr[i][j] == 1:
                    cnt1 += 1
                if arr[i][j] == 2:
                    cnt2 += 1

    print('#{} {} {}'.format(tc, cnt1, cnt2))



        # 가로 변환 검사 돌을 놓는 순간 그줄만 검사하면됨.. y줄
        # tmp = []
        # tmp_idx = []
        # for k in range(n+1):
        #     if arr[y][k]:
        #         tmp.append(arr[y][k])
        #         tmp_idx.append(k)
        # if tmp:
        #     if tmp[0] == tmp[-1]:
        #         for a in range(len(tmp)):
        #             arr[y][tmp_idx[a]] = tmp[0]
        # # 세로 변환 검사 x줄만..
        # tmp = []
        # tmp_idx = []
        # for k in range(n + 1):
        #     if arr[k][x]:
        #         tmp.append(arr[k][x])
        #         tmp_idx.append(k)
        # if tmp:
        #     if tmp[0] == tmp[-1]:
        #         for a in range(len(tmp)):
        #             arr[tmp_idx[a]][x] = tmp[0]
        # # 대각선 검사...
        # tmp = []
        # tmp_idx = []
        # for k in range(n + 1):
        #     if arr[k][x]:
        #         tmp.append(arr[k][x])
        #         tmp_idx.append(k)
        # if tmp:
        #     if tmp[0] == tmp[-1]:
        #         for a in range(len(tmp)):
        #             arr[tmp_idx[a]][x] = tmp[0]
        # print('{}: dol({},{} color{}) : {}'.format(i, x, y, color, arr))


    # print(arr)
    #
