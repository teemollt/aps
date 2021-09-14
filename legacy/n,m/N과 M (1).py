# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
def sol(v, d):
    global visited
    # 방문처리
    visited[v] = 1
    d += 1
    print(v, end=" ")
    # 종료 조건 m개 뽑았을때
    if d == m:
        print()
        return
    # 다음거 뽑기
    for i in range(1, n+1):
        # 방문 하지 않은거면 뽑기
        if not visited[i]:
            sol(i, d)
            # 빠져나오면 방문 취소
            visited[i] = 0




n, m = map(int, input().split())
numbers = list(range(1, n))
visited = [0] * (n+1)
for i in range(1, n+1):
    sol(i, 0)
    visited[i] = 0