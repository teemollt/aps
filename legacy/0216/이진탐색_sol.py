def find_cnt(page, target):
    s = 1
    e = page
    c = int((s+e)/2)
    cnt = 0
    # c에 위치한 숫자가 내가 찾는 숫자가 아니면 계속 찾는것을 반복
    while c != target:
        if target > c:
            s = c
        else:
            e = c
            cnt += 1
            c = int((s + e) / 2)
    return cnt


t = int(input())
for tc in range(1, t+1):
    p, a, b = map(int, input().split())
