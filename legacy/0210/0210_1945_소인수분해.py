import sys
sys.stdin = open("input (3).txt")
t = int(input())
for tc in range(1, t+1):
    n = int(input())

    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5 # 정답을 위한 개수 세기

    # 주어진 소수의 수만큼 반복
    for i in range(len(prime)):
        while n % prime[i] == 0:
            cnt[i] += 1
            n //= prime[i]

    print('#{} {}'.format(tc, " ".join(map(str, cnt))))