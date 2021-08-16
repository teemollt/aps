import sys, heapq
input = sys.stdin.readline
l, r = [], []
n = int(input())
for i in range(n):
    x = int(input())
    # 양쪽 리스트 길이가 같으면 왼쪽에 최대힙으로 먼저 삽입
    if len(l) == len(r):
        heapq.heappush(l, (-x, x))
    # 왼쪽에 하나더 많으면 오른쪽에 최소힙으로 삽입
    else:
        heapq.heappush(r, (x, x))
    # 좌우에 번갈아가면 왼쪽엔 최댓값이, 오른쪽엔 최솟값이 루트에 오도록 추가 해준 상태
    # 좌측 최댓값이 곧 전체 값들의 중간값이 되도록하는것.
    # 그런데 왼쪽 최댓값보다 오른쪽 최솟값이 더 크면 순간적으로 중간값이 오른쪽 최솟값에 들어있는 것이므로
    # 둘을 바꿔서 중간값이 좌측 최댓값에 들어가도록 만들어줘야함.
    if r and l[0][1] > r[0][1]:
        rn = heapq.heappop(r)[1]
        ln = heapq.heappop(l)[1]
        heapq.heappush(l, (-rn, rn))
        heapq.heappush(r, (ln, ln))
    print(l[0][1])



