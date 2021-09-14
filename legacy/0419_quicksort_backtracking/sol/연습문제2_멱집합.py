# 모든 부분집합(멱집합) 구하기
#각 요소들이 부분집합에 포함되는 경우/되지 않는 경우를 모두 고려
# idx : 부분집합에 포함여부를 결정하려고 하는 요소의 idx
#selected : 각 idx의 요소가 부분집합에 포함되는지 표시하는 배열
# ex) [0,1,0,1,0] : 1번요소와 3번요소가 부분집합에 포함
arr = [1,2,3,4,5,6,7,8,9,10]   # [2, 4]
N = 10
#result : 중간 결과
def power_set(idx,selected,result):
    global cnt,tmp_cnt
    if result > 10: #정답이 될 수 없음,가지치기
        return
    tmp_cnt += 1
    if idx == N:    #인덱스 끝까지 포함여부를 결정했음
        #집합 중에서 원소의 합이 10인 부분집합
        sum_v = 0
        tmp = list()
        for i in range(N):  #부분집합 선택이 되었으면, 요소 더하기
            if selected[i]== 1:
                sum_v += arr[i]
                tmp.append(arr[i])
        if sum_v == 10: #요소의 합이 10인지 확인
            result_list.append(tmp)
            cnt += 1
        return
    #모든 경우의 수를 다 고려
    #현재 idx의 요소가 부분집합에 포함
    #포함되지 않느냐
    #경우의 수를 표시하기 위해서...selected 배열을 사용
    selected[idx] = 1   #현재 idx 요소 부분집합 포함
    #다음요소 포함여부 결정
    power_set(idx + 1,selected,result + arr[idx])
    selected[idx] = 0   #현재 idx 요소 부분집합 미포함
    # 다음요소 포함여부 결정
    power_set(idx + 1, selected,result)

tmp_cnt = 0
cnt = 0
selected = [0] * N
result_list = list() #부분집합 요소의 합이 10인 부분집합을 저장할 리스트
power_set(0,selected,0)
# print(cnt)
# print(tmp_cnt)
for row in result_list:
    print(row)