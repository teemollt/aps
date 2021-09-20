n = int(input())
used = [-1]*n    # 인덱스 행의 몇번째 열에 놓여있는지를 값에 넣기
cnt = 0
def sol(d, used):
    global cnt
    if d == n:
        cnt += 1
        return
    for i in range(n):
        if i not in used:
            for k in range(n):
                if used[k] > -1 and abs(k - d) == abs(used[k] - i):
                    break
            else:
                used[d] = i
                sol(d+1, used)
                used[d] = -1
sol(0, used)
print(cnt)
# pypy로 해야 통과됨...