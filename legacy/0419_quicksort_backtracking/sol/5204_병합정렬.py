#merge_sort : 대상 배열을 정렬하고, 반환하는 함수
#arr : 정렬하고자 하는 대상 배열
def merge_sort(arr):
    #배열의 길이가 1이라면, 정렬할 필요가 없음
    if len(arr) == 1:
        return arr
    mid = len(arr)//2   # 문제에서 주어진 중간값
    #두 가지 부분으로 나뉨
    #1. 전체를 두 부분으로 나누어서 각각 정렬
    # 왼쪽 0~mid-1
    left = arr[:mid]
    left = merge_sort(left)
    # 오른쪽 mid~끝
    right = arr[mid:]
    right = merge_sort(right)
    #2. 나뉘어진 두 부분을 크기순서대로 합병 : merge
    return merge(left,right)

def merge(left,right):
    global cnt
    #두 배열을 합치기
    i=j=0
    #두 배열을 합친 결과 배열
    result = list()
    # 복사할 배열 요소가 남아있으면 계속 반복
    left_len = len(left)
    right_len = len(right)
    #문제에서 요구한 정답, 왼쪽배열의 마지막 요소가 더 큰 경우
    if left[-1] > right[-1]:
        cnt += 1

    while i<left_len or j < right_len:
        #1. left와 right에 모두 복사할 요소가 남아있는경우
        #2. left에만 남아있는 경우
        #3. right에만 남아있는경우
        if i < left_len and j < right_len:  #1번
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i< left_len:   #왼쪽 요소만 남음..
            result.append(left[i])
            i += 1
        elif j < right_len: #오른쪽 요소만 남음
            result.append(right[j])
            j += 1
    return result


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    result = merge_sort(arr)
    print("#{} {} {}".format(tc,result[N//2],cnt))