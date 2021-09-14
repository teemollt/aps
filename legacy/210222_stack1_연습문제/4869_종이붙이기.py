def solve(x):
    if x == N:
        return 1
    if x > N:
        return 0

    return solve(x + 10) + solve(x+20)*2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = solve(0)
    print("#{} {}".format(tc,result))
















    pass