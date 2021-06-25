# merge_sort
#


def merge(l, r):
    # 각 리스트에서 사용할 인덱스 i, j, 병합리스트 s
    i = j = 0
    s = []
    # 두 리스트 중 하나 끝까지 갈때까지 반복
    while i < len(l) and j < len(r):
        # 둘중 더 작은거 먼저 결과리스트에 담기
        if l[i] < r[j]:
            s.append(l[i])
            i += 1
        else:
            s.append(r[j])
            j += 1
    # 위에서 둘중 하나의 리스트 요소만 다 사용됨
    # 남은 리스트 요소들 다 뒤에붙여줘야함
    # i가 끝까지 가있으면
    # l의 모든 요소는 다 병합됐으므로
    if i == len(l):
        # s에 r의 남은 모든 요소 이어 붙여주기
        s += r[j:]
    else:
        s += l[i:]
    return s

def merge_sort(arr):
    # 리스트의 길이가 1이하면 더이상 나눌수 없으므로 리턴
    if len(arr) <= 1:
        return arr
    # 아니면 반으로 리스트 나눠서 재귀
    mid = len(arr) // 2
    # 좌우 리스트 나눠주기 재귀로 조건에 걸릴때까지
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid: len(arr)])
    # 좌우 리스트 병합
    return merge(l, r)

arr = [1,4,5,2,4,5,2,2,50,3,456,24,623,7,457,52,50]
print(arr)
print(merge_sort(arr))