arr = [[0] * 5 for _ in range(5)]
N = 5
cnt = 1
# 특정조건일 때 계속 반복 : while
# 반복 횟수가 정해져 있으면  for : 배열의 길이만큼, 요소의 개수만큼
#모든 칸이 숫자로 채워질 때 까지 반복
total = N*N
#r,c는 숫자를 입력하려고 하는 좌표값
r = 0
c = 0
dr = [0,1,0,-1]
dc = [1,0,-1,0]
dir = 0 # 시작 방향이 오른쪽이니까 0부터 시작
#좌측 상단에서 시작, (0,0) 에서 시작
while cnt <= total:
    if 0<=r < N and 0<=c <N and not arr[r][c]:
        arr[r][c] = cnt
        cnt += 1
    else: #방향이동이 필요함
        r -= dr[dir]
        c -= dc[dir]
        dir = (dir + 1) % 4
    #숫자 넣었으니 이동, 현재 이동방향으로 변화량 더하기
    r += dr[dir]
    c += dc[dir]
    # print("!!!!!")

#출력 부분
for i in range(N):
    for j in range(N):
        # arr[i][j] = cnt
        # cnt += 1
        print(arr[i][j],end = " ")
    print()