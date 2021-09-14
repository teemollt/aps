#이차원 배열에서의 BFS
arr = [[1,1,0,0,0,0],
       [0,1,1,1,1,0],
       [0,0,3,0,1,1],
       [0,0,2,0,1,0],
       [0,0,1,1,1,0],
       [0,0,0,0,0,0]]
N = 6
#3에서 시작 2에서 도착
#상하좌우로 연결되어 있고, 1인경우에만 이동가능
#r,c :  시작정점
def bfs(r,c):
    #이차원 배열에서는 정점의 구분을 좌표로 해야 한다.
    queue = list()
    visited = [[0] * N for _ in range(N)]
    #(r,c,d) ,
    # r,c :현재좌표
    # d : 시작시점으로 부터 거리
    queue.append((r,c,0))
    visited[r][c] = 1
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    #1. 방문하는 정점을 queue에서 dequeue하고, 
    #2. 갈 수 있는 경로가 있으면 queue에 enQueue,
    #3. queue가 빌때까지 1,2를 반복

    #도착지까지 거리구하기
    #queue에 현재 좌표만 저장하는게 아니라
    #현재 거리 정보도 같이 저장
    while queue:
        #cd : 현재까지 거리
        cr,cc,cd = queue.pop(0)
        print((cr,cc,cd))
        if arr[cr][cc] == 2:
            print("도착","거리는: ",cd)
        #cr,cc에서 방문할 수 있는 경로 탐색하기
        #사방탐색: 상,하,좌,우
        for d in range(4):
            #nr, nc : 탐색하고자 하는 방향에 있는 좌표
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<=nr<N and 0<=nc < N and  arr[nr][nc] != 0 and visited[nr][nc] == 0:
                #방문할 수 있으니, queue넣고
                #방문했음을 표시
                #cd+1 : 현재 위치까지 거리가 cd니까...다음위치 까지 거리는 cd+1
                queue.append((nr,nc,cd+1))
                visited[nr][nc] = 1
bfs(2,2)