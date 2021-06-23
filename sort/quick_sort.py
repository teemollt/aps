# Quicksort is a divide-and-conquer algorithm.
# It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
# according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort.
# Best-case performance: O(n log n)
# Worst-case space complexity: O(n)
# 기준보다 작은건 왼쪽 큰건 오른쪽으로 반복

def quick_sort(arr, start, end):
    # start가 end보다 크거나 같으면 요소가 1개 이하이므로 종료
    if start >= end:
        return
    # 임의로 1번째 요소 pivot으로
    # hoare_partition
    pivot = start
    # 왼쪽 pivot 다음 요소부터
    l = start + 1
    # 오른쪽 end
    r = end
    # 왼쪽보다 오른쪽이 큰동안 반복
    while l <= r:
        # l 한칸씩 오른쪽으로 옮기면서 pivot보다 큰거 찾을때까지 반복
        # 바로 아래에서 < 을 쓰면 아래 조건문(if l > r)을 통과 못하는 경우 발생
        # (pivot보다 큰걸 찾지못해서 l이 end까지 가고 r이 end와 같은경우:
        # 이경우 l이 end와 같아져도 + 1 해줌으로써 if l > r을 통과하게 해줌
        # 둘다 pivot과 같은값에서도 멈추게 하면 무한푸프 빠짐 pivot과 같은값에서 멈출 필요 없음
        while l <= end and arr[l] <= arr[pivot]:
            l += 1
        # r 한칸씩 왼쪽으로 옮기면서 pivot보다 작은거 찾기
        while r > start and arr[r] >= arr[pivot]:
            r -= 1
        # l과 r의 교차가 기준
        # (l과 r 위치가 교차된 순간 r의 위치를 기준으로 r을 포함한 r의 왼쪽은 pivot보다 모두 작고 r의 오른쪽은 pivot보다 모두 크므로
        # r과 pivot의 위치를 바꿔주면 pivot을 중심으로 좌우 정렬이 된다.)
        # l,r 이동이 다 끝나고 l과 r 위치가 교차되었다면 pivot과 r의 위치 교환 (정렬이 된 상태)
        if l > r:  # >=를 쓰면 가장 위 while문 무한루프 발생할 수 있음
            arr[r], arr[pivot] = arr[pivot], arr[r]
        # 교차되지 않았으면 l, r 위치 교환 (아직 정렬이 덜된 상태)
        else:
            arr[l], arr[r] = arr[r], arr[l]
    # 한번 pivot을 기준으로 좌우를 정렬했으면
    # 좌우 각각 같은 작업을 재귀로 실행해줌
    # 왼쪽 시작점은 start, 끝점은 r
    # (값은 바꿔줬지만 위치 idx가 저장되어 있는 r과 pivot은 바꾸지 않았으므로 r이 그자리를 가리키고 있다)
    quick_sort(arr, start, r-1)
    # 오른쪽 r이 가리키고 있는 자리를 기준으로 좌우를 나눠줬으므로 r위치는 빼고 각각 정렬하면됨.
    quick_sort(arr, r+1, end)
    # 재귀 종료되면 arr 리턴
    return arr

arr = [5,3,2,1,1,54,5,3,3,1,5,47,56,35,23,4]
arr2 = [5,4,3,2,1]
arr3 = [1,1,2,1,1]
# print(arr)
print(quick_sort(arr3, 0, len(arr3)-1))
