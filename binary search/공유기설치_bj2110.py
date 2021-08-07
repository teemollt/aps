# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi

n, c = map(int, input().split())
xs = [int(input()) for _ in range(n)]
xs.sort()
# 양쪽끝에 라우터 놓고 이분탐색으로 가운데 인덱스 거리 양옆으로 잰다음
# 저장해놓고 양쪽중에 더 먼쪽으로 다시 이분탐색
l, r, c = 0, n-1, c-2
router = [xs[l], xs[r]]
while c:
    while l <= r:
        mid = (l+r) // 2
        l_gap, r_gap = xs[mid] - xs[l], xs[r] - xs[mid]
