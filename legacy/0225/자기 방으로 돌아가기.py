import sys
sys.stdin = open("sample_input (room).txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 위아래로 나뉘어 있으므로 가운데 통로는 200개
    visited = [0] * 200
    for i in range(n):
        l, r = map(int, input().split())
        if l % 2:
            s = l // 2
        else:
            s = l // 2 - 1
        if r % 2:
            e = r // 2
        else:
            e = r // 2 - 1
        if s < e:
            for j in range(s, e+1):
                # 가운데 통로를 방문처리
                visited[j] += 1
        else:
            for j in range(e, s+1):
                visited[j] += 1
    max_v = 0
    for i in range(len(visited)):
        if visited[i] >= max_v:
            max_v = visited[i]
    print('#{} {}'.format(tc, max_v))




