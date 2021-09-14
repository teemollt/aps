def sol(x):
    # 한칸 씩 이동하면서 부분행렬의 시작점 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                # 가로길이, 세로길이 구하기
                col_cnt = 0
                row_cnt = 0
                for k in range(j, n):
                    if arr[i][k] != 0:
                        col_cnt += 1
                    else:
                        break
                for k in range(i, n):
                    if arr[k][j] != 0:
                        row_cnt += 1
                    else:
                        break
