arr = [[0]*5 for _ in range(5)]
n = 5
cnt = 1

# 특정 조건일때 계속 반복 : while
# 반복 횟수가 정해져 있으면 : for  배열의 길이만큼, 요소의 개수만큼...
# 모든 칸이 숫자로 채워질때 까지 반복
end = n*n
# r, c는 숫자를 입력하려고 하는 좌표값
r = 0
c = 0
# 델타 우하좌상 순으로
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 시작방향 오른쪽이니 0부터 시작
dir = 0
# 좌측 상단에서 시작, 0, 0
while cnt <= end:
    # 인덱스에러 노노
    if 0 <= r < n and 0 <= c < n and not arr[r][c]:
        arr[r][c] = cnt
        cnt += 1
        # 방향이동 필요
    else:
        # 이미 한칸 가버렸으니 다시 빼줘서 돌려놓고 방향바꾼뒤 다시 한칸.
        r -= dr[dir]
        c -= dc[dir]
        dir = (dir + 1) % 4  # % 이용해서 루프 돌기....
        # 숫자 넣었으니 이동, 현재 이동방향으로 변화량 더하기
    r += dr[dir]
    c += dc[dir]


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()