import sys
sys.stdin = open("sample_input (omok).txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = ['.'*(n+2)] + ['.' + input() + '.' for _ in range(n)] + ['.'*(n+2)]
    dx = [1, 1, 0, -1]
    dy = [0, 1, 1, 1]
    rst = 'NO'
    # print(arr)
    for i in range(n):
        for j in range(n):
            for dir in range(4):
                if arr[i][j] == '.':
                    break
                else:
                    num = 0
                    cnt = 0
                    while  arr[i + dy[dir] * num][j + dx[dir] * num] != '.':
                        cnt += 1
                        num += 1
                        if cnt == 5:
                            rst = 'YES'
                            break

    print(rst)








