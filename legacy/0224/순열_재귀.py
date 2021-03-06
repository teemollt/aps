N = 4
arr = [1,2,3,4]
#깊이우선탐색(재귀)으로 순열구하기
#used : 수열의 각 요소가 순열을 만드는데 사용되었는지 표시하는 배열
used = [0] * N
#만드는 순열들을 저장하는 배열
perm_arr = [0] * N
#idx : 순열에 포함되는 숫자를 결정하기 위한 인덱스
def perm(idx,used,N):
    global perm_arr
    #모든 인덱스에 해당하는 숫자가 결정되었다(인덱스가 벗어남)
    if idx == N:
        print(perm_arr) #출력

    #현재 인덱스에서 할 수 있는 일은...
    #앞에서 사용되지 않은 숫자를 모두 해당 인덱스에 넣어보는것
    for i in range(N):
        if not used[i]: #i 번째 요소가 아직 사용되지 않았으면

            perm_arr[idx] = arr[i]  #idx 번째 숫자에 i번째 숫자 할당
            used[i] = 1 #i번째 숫자 사용했음을 표시
            perm(idx+1,used,N)   #다음 idx를 결정

            # i번째 숫자를 사용하고 나서 이후 과정을 수행했으므로,
            # 현재 idx에 다른 숫자를 넣어주기 위해서 i번째 숫자는
            # 사용이 끝난 것, 사용하지 않은 것으로 표시
            used[i] = 0
#실행
#0번 인덱스부터 숫자를 결정해야 하니, 0을 넣어줌
perm(0,used,N)





