# 퀵 정렬을 구현해봅시다.
# 분할 정복 알고리즘의 대표적인 알고리즘
# partition : pivot을 기준으로 큰값과 작은값으로 나누고
# quick_sort : 작은값 부분과, 큰값 부분을 다시 퀵정렬 한다.
#hoare_partition : 가장 앞이나, 뒤, 중간 중에서 pivot을 잡아주고
# 양쪽끝에서 인덱스를 각각 하나씩 줄여가면서 pivot과 비교 및 교환하는 알고리즘
# 실행결과 : pivot의 위치를 반환, 함수 실행뒤에는 전체가 pivot을 기준으로
#        큰 값과 작은 값으로 분리된다.
def hoare_partition(arr,start,end):
    # pivot을 설정하고,
    pivot = arr[start]  #영역의 가장 왼쪽 값을 pivot으로 임의 설정
    i = start   # 오른쪽으로 한 칸씩 이동하면서, pivot 보다 큰 값의 인덱스에서 정지
    j = end     # 왼쪽으로 한 칸씩 이동하면서, pivot 보다 작은 값의 인덱스에서 정지
    # pivot보다 큰 값과, 작은 값으로 영역구분
    while i <= j:
        #i는 증가하면서 pivot 보다 큰 값 찾기
        while i<= j and arr[i] <= pivot:
            i += 1
        #j는 감소하면서 pivot 보다 작은 값 찾기
        while arr[j] > pivot:
            j -= 1
        #찾았으면, i와 j의 위치교환(목적: 큰 값을 뒤로 보내기)
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]
    #pivot의 자기 자리 찾아주기, 작은값중에 제일 뒤에 있는 애랑 바꿔주면 됩니다.
    arr[start], arr[j] = arr[j], arr[start]
    # pivot의 위치를 반환
    return j

#pivot 보다 큰값과 작은값으로 전체를 분리해서 각각 다시 quick_sort를 수행
#start :왼쪽 시작 인덱스   end:오른쪽 끝 인덱스
def quick_sort(arr, start,end):
    if start >= end:    #나뉘어진 부분의 크기가 1이하이면 재귀 호출 불필요
        return
    pivot = hoare_partition(arr,start,end)
    #작은쪽 : start~pivot-1
    quick_sort(arr, start,pivot-1)
    #큰쪽 : pivot + 1 ~ end
    quick_sort(arr, pivot+1,end)


arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
quick_sort(arr,0,len(arr)-1)
print(arr)