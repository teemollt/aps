# def move():
#     r += dr[d_idx]
#     c += dc[d_idx]
#     arr[r][c] = i



n = 5
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
arr = [[0]*n for i in range(n)]
r = 0
c = 0
d_idx = 0
for i in range(n**2):
    # 인덱스가 끝에 닿거나/다음 인덱스에 이미 숫자가 들어있는 경우 방향 전환.
    # 끝에 닿을때 => 인덱스가 어느한쪽이 0 or 4
    if (r == 0 and c == 0) or (r == 0 and c == 4) or (r == 4 and c == 4) or (r == 4 and c == 0):
        if d_idx < 4:
            d_idx += 1
        else:
            d_idx = 0
        r += dr[d_idx]
        c += dc[d_idx]
    elif arr[r+dr[d_idx]][c+dc[d_idx]]:
        if d_idx < 4:
            d_idx += 1
        else:
            d_idx = 0
        r += dr[d_idx]
        c += dc[d_idx]


    else:
        r += dr[d_idx]
        c += dc[d_idx]
        arr[r][c] = i

print(rst)