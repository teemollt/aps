N = 5
arr = [1,2,3,4,5]
#각 집합 요소가, 부분집합에 포함되는지 표시하는 배열
selected = [0] * N
#idx : 현재 포함여부를 결정하려고 하는 인덱스 번호 
#N : 전체 집합의 요소 개수
def power_set(idx,N):
    # 모든 인덱스에 대해서 요소의 부분집합 포함여부를 결정
    if idx == N:
        # print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i],end=" ")
        print()
        return
    #아직 결정 덜했다!
    #내가 할 수 있는 모든 경우의 수를 모두 수행하기
    #idx에 해당하는 요소가 부분집합에 포함 될거냐/ 말거냐를 결정
    selected[idx] = 1
    power_set(idx+1,N)
    selected[idx] = 0
    power_set(idx+1,N)
power_set(0,N)
