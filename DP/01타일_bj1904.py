# n-1 경우의수 + n-2 경우의수가 n 경우의 수가 된다는 규칙을 찾으면 쉬움...
# % 15746을 굳이 문제에서 시킨 이유는 dp를 쓰면서 매번 값을 저장할때마다 % 안해주면 메모리 초과가 나기때문인듯...
arr = [0]*1000001
arr[1], arr[2] = 1, 2
def sol(n):
    for i in range(3, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 15746
    return arr[n]
n = int(input())
print(sol(n))