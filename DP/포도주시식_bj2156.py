def sol():
    n = int(input())
    m = [int(input()) for _ in range(n)]
    arr = [0] * (n+1)
    arr[1] = m[0]
    if n > 1:
        for i in range(2, n+1):
            # 3잔을 연속으로 마실 수 없음
            # 1,2,3번 잔 => 1번+3번 마심/2번+3번마심/2번 마심
            arr[i] = max(m[i-1]+arr[i-2], m[i-1]+m[i-2]+arr[i-3], arr[i-1])
    print(arr[n])
sol()