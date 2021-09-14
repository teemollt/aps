# 선택정렬 잘 알아둬~

arr = [5, 4, 2, 1, 3, 7, 6]

def selection_sort():
    # 들어갈 자리에 맞는 숫자 선택해서 넣어주기
    # 어떤 자리에 숫자가 들어갈지에 대한 반복문.
    for i in range(len(arr) - 1): # 정렬하면 맨마지막 자리는 자동으로 정렬이 되어있으므로 -1해줘도됨
        # 각 자리에 맞는 숫자 어케 찾음?
        # 배열 순회 하면서 제일 작은거 찾기
        # 단 시작점은 현재 자리부터
        min_v = arr[i] # 최소값 초기화
        min_p = i   # 최소값 위치 초기화
        for j in range(i+1, len(arr)):
            if arr[j] < min_v:
                min_v = arr[j]
                min_p = j
        # 반복문이 끝나면 min_v, min_p
        # 에 최소값과 최소값의 위치가 저장
        arr[i], arr[min_p] = arr[min_p], arr[i]
    print(arr)

selection_sort()