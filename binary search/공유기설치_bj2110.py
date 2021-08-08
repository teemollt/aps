# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi
from sys import stdin
n, c = map(int, stdin.readline().split())
xs = [int(stdin.readline()) for _ in range(n)]
xs.sort()
# 최소갭, 최대갭 1, 각끝 자리
min_g, max_g = 1, xs[-1] - xs[0]
while min_g <= max_g:
    mid = (min_g+max_g)//2
    # 출발점 1은 무조건 찍고 시작하니까 cnt 1
    cnt = 1
    # 공유기 설치할 수 있는 가장 가까운 위치 초기화
    cl = xs[0] + mid
    for i in xs:
        # 공유기 설치하는 위치보다 현위치 i가 멀거나 같다면 카운트.
        if cl <= i:
            cnt += 1
            # 공유기 설치했으니 공유기 설치 가능 위치 재조정
            cl = i + mid
    # cnt가 c보다 크거나 같다면
    if cnt >= c:
        # 최소갭을 up시켜서 설치가능한 최소거리 위치를 늘려보자
        min_g = mid+1
    else:
        # cnt에 도달하지 못했다면 설치 가능거리를 너무 멀게 잡은거니까 짧게 좁혀주자
        max_g = mid-1
print(max_g)
