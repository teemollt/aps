# 이진탐색 반으로 쪼개면서 절반 버리고 탐색
# 정렬된 상태에서..
# cnt는 확인용..
cnt = 0
def search(arr, target, s, e):
    global cnt
    # 시작점이 끝점보다 커지면 찾는 값이 없는것
    cnt += 1
    if s > e:
        return None
    # 중간점
    mid = (s+e)//2
    # 중간점이 찾는 값이면 위치 리턴
    if arr[mid] == target:
        return mid
    # 중간값과 찾는값 비교해서 좌 or 우에서 다시 재귀로 함수 실행
    elif arr[mid] > target:
        # 가장 안쪽으로 들어가서 결과값을 찾아야 하니까 리턴으로 다시 안나오게하는건가
        return search(arr, target, s, mid-1)
    else:
        return search(arr, target, mid+1, e)

arr = [2,4,6,9,12,15,17,23,27,32,37,39,40,50]
target = 12
print(search(arr, target, 0, len(arr)), cnt)