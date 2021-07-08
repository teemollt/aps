# 몸무게 x 키 y (x, y) x,y 둘다 더커야 덩치가 큰거

n = int(input())
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

rank = ""
for i in range(n):
    cnt = 0
    for j in range(n):
        if p[i][0] < p[j][0]:
            if p[i][1] < p[j][1]:
                cnt += 1
    print(cnt+1, end=" ")