#1. 부분행렬 크기 찾기
def search():
    global cnt      #cnt :부분행렬의 개수를 저장하는 변수
    #한 칸 씩 이동하면서 부분행렬의 시작점을 찾음
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:  #부분행렬의 시작
                cnt += 1
                #가로길이, 세로길이 구하기
                col_cnt = 0
                row_cnt = 0
                #j부터 0이 나오기 까지 개수 세기
                for k in range(j,N):
                    if arr[i][k] != 0:
                        col_cnt += 1
                    else:
                        break
                #i부터 0이 나오기 전까지 개수 세기 
                for k in range(i,N):
                    if arr[k][j] != 0:
                        row_cnt += 1
                    else:
                        break
                #가로세로 길이를 구했으니 저장
                #(세로,가로,넓이)
                mlist.append((row_cnt,col_cnt,row_cnt*col_cnt))
                #저장된 영역은 다시 검사하는것을 방지하기 위해서, 0으로 바꾸어줌
                for k in range(i,i+row_cnt):
                    for l in range(j,j+col_cnt):
                        arr[k][l] = 0

#2. 크기별로 정렬하기
def bSort():
    #크기별로 오름차순 정렬, 만약에 넓이가 같으면, 행의 크기가 작으면 작은걸로 판단
    #버블소트 : 넓이가 넓고, 행의 크기가 크면 뒤로 보내기
    for i in range(cnt-1):
        for j in range(0,cnt-i-1):
            #넓이가 넓으면 뒤로 보내기
            if mlist[j][2] > mlist[j+1][2]:
                mlist[j], mlist[j+1] = mlist[j+1],mlist[j]
            #넓이가 같다면, 행의 크기가 큰 값을 뒤로 보내기
            elif mlist[j][2] == mlist[j+1][2]:
                 if mlist[j][0] > mlist[j+1][0]:
                     mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mlist = list()  #찾아낸 행렬정보를 저장
    cnt = 0 #찾은 부분행렬의 개수
    search()
    bSort()
    print("#{} {}".format(tc,cnt),end = " ")
    for i in range(cnt):
        print("{} {}".format(mlist[i][0],mlist[i][1]),end=" ")
    print()