import sys
sys.stdin = open("sample_input (2).txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    # n*n 크기 글자판
    arr = [[] for _ in range(n)]
    # 입력
    for i in range(n):
        a = input()
        for j in range(len(a)):
            arr[i].append(a[j])


    rst = ""
    for i in range(n):
        for j in range(n-m+1):
            row, r_row = [], []
            col, r_col = [], []
            for k in range(j, j+m):
                row.append(arr[i][k])
                col.append(arr[k][i])
            for q in range(j+m-1, j-1, -1):
                r_row.append(arr[i][q])
                r_col.append(arr[q][i])
            if row == r_row:
                for chr in row:
                    rst += chr
                break
            if col == r_col:
                for char in col:
                    rst += char
                break

    print('#{} {}'.format(tc, rst))