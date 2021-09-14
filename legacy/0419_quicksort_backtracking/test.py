# 기다리는 사람수 n
# 심사관의 수, 심사관이 심사하는데 걸리는 시간 리스트 times
n = 6
rst = 0
times = [7, 10]
c = len(times)
times.sort()
print(times)
# 1분씩 흐르면서 반복문으로 처리 시간만큼
m = 0
if n > c:
    while n:
        m += 1
        for i in range(c):
            if not m % times[i]:
                n -= 1
            if n == 0:
                break
else:

print(m)


