# 재귀로 순열
# 재귀 한번 호출시 각 idx별 숫자가 어디에 들어갈지 결정
# 어떤 요소의 위치를 결정할지 idx 필요
# 어떤위치가 사용되었는지 정보 필요 => used
# 순열을 저장하는 배열 : arr
# 요소의 개수 N
arr = [1,2,3,4,5]
used = [0,0,0,0,0]
N = 5
newArr = [0] * N
def perm(p, used, idx, N):
    if idx == N:
        print(p)
        return
    # 해당 인덱스의 요소가 들어갈 수 있는 칸 찾기
    # used를 순회하면서 0이면 사용 안한거, 1이면 사용한거
    for i in range(N):
        if used[i] == 0:
            p[i] = arr[idx]
            used[i] = 1
            # 다음요소 자리 결정
            perm(p, used, idx+1, N)
            # 요소 다썼으니 반납
            used[i] = 0

perm(newArr, used, 0, N)