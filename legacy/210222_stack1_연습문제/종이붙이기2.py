N = 40
cnt = 0
#내가 원하는 길이가 되면, cnt를 1증가 시키는 함수
def solve(l):
    global cnt
    if l > N:
        return 0
    elif l == N:
        return 1
    #무슨뜻?? N보다 작으니까 아직 우리가 원하는 길이가 안됨
    #종이를 더해주면 된다.
    #10짜리를 더해주기 1번
    # 20짜리 더해주기 2번
    return solve(l+10) + solve(l + 20)* 2

#해당 길이의 종이를 만들 수 있는 개수를 반환하는 함수
def solve2(l):
    if l == 0:
        return 1
    elif l == 10:
        return 1
    ######종이의 길이가 10초과인 상황
    #20부터는   나보다 10작은 종이의 개수 + 20작은종이의 개수*2
    return solve2(l-10) + solve2(l-20)*2

# print(solve(0))
print(solve2(40))

