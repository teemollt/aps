# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
#
# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
#
# 둘째 줄에는 중앙값을 출력한다.
#
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
#
# 넷째 줄에는 범위를 출력한다.
def avg(arr):
    s = 0
    for i in arr:
        s += i
    return s // len(arr)

def midv(arr):
    arr.sort()
    m = len(arr)//2
    return arr[m]

def oft(arr):
    tmp = list(set(arr))
    cnt = []
    for i in tmp:
        cnt.append((arr.count(i), i))
    mv = max(cnt)
    c = 0
    cv = []
    for i in cnt:
        if mv[0] == i[0]:
            c += 1
            cv.append(i[1])
    cv.sort()
    if c > 1:
        return cv[1]
    return mv[1]

def ran(arr):
    arr.sort()
    return abs(arr[-1] - arr[0])

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
leng = len(nums)
print(round(sum(nums)/leng))
mid = leng//2
print(nums[mid])
oft = sorted(list(set(nums)))
mct = 0
for i in range(len(oft)):
    cnt = nums.count(oft[i])
    if cnt > mct:
        rst = oft[i]
        mct = cnt
    elif cnt == mct:
        rst = oft[i]
        break
print(rst)
print(abs(nums[-1]-nums[0]))

