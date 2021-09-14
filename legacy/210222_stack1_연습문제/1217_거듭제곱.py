#tmp : 중간결과
#cnt : 곱한 횟수
def solve(tmp,cnt):
    if cnt == M:
        return tmp
    return solve(tmp*N,cnt+1)

for _ in range(10):
    tc = int(input())
    N,M = map(int,input().split())
    print("#{} {}".format(tc,solve(1,0)))