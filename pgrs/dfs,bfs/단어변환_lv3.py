def bfs(n, begin, target, words):
    rst = 987654321
    q = []
    used = [0] * len(words)
    q.append((begin, 0, used))
    while q:
        w, d, u = q.pop(0)
        if w == target:
            if d < rst:
                rst = d
        for i in range(len(words)):
            if not u[i]:
                cr = [0] * n
                for j in range(n):
                    if words[i][j] == w[j]:
                        cr[j] = 1
                if sum(cr) == n-1:
                    u[i] = 1
                    q.append((words[i], d+1, u))
    return rst

def solution(begin, target, words):
    answer = 0
    n = len(begin)
    answer = bfs(n, begin, target, words)
    if answer == 987654321:
        return 0
    return answer