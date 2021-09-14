#흰색,파란색, 빨간색 영역으로 구분해야하는데
#세 영역으로 구분하려면, 2개의 구분선이 필요
# 구분선의 값(행의 인덱스)을 2개 선택해주면 된다.
# 전체행에서 마지막줄을 제외하고, 2개 선택하는거니까..
# 전체집합에서 요소 2개선택하는 조합이다.
#그러면 조합 만들어 보아요..
#idx : 자르려고 하는 행의 번호
#cnt : 몇개의 행을 잘랐는지 세는 변수
#selected : 자른 행을 저장하는 배열
def comb(selected,idx,cnt):
    global min_v
    if cnt == 2:
        #모든 선택이 끝난 상황
        # print(selected)
        #수정해야하는 개수를 카운팅
        # selected[0] >>> 흰색 구분선
        # selected[1] >>> 파란색 구분선
        a = selected[0] #첫 번째 구분선
        b = selected[1] #두 번째 구분선
        #흰색영역 0~ a
        cnt = 0
        for i in range(0,a+1):
            for j in range(M):
                if flag[i][j] != 'W':
                    cnt += 1
        #파란색영역  a+1~b
        for i in range(a+1,b+1):
            for j in range(M):
                if flag[i][j] != 'B':
                    cnt += 1
        #빨간색 영역 b+1~ 끝까지
        for i in range(b+1,N):
            for j in range(M):
                if flag[i][j] != 'R':
                    cnt += 1

        #개수를 구했으니 최소 개수인지 확인
        if cnt < min_v:
            min_v = cnt
        return
    if idx == N-1: # 마지막줄은 구분선이 될 수 없음
        return
    #각 행을 자를건지 말건지 결정
    #idx행을 자르기
    selected[cnt] = idx #자른 행을 저장
    comb(selected, idx+1, cnt+1)
    #idx행을 안자르기
    comb(selected, idx+1, cnt)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    flag = [input() for _ in range(N)]
    # 깃발 색칠 최소값
    min_v = 2500    #N * M이 최대 2500개
    selected = [-1] * 2
    comb(selected,0,0)
    print("#{} {}".format(tc,min_v))
# N = 4
# #selected 의 값은...구분선으로 사용하려는 행번호가 들어감
# selected = [-1] * 2
# comb(selected,0,0)