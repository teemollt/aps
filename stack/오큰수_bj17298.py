# 문제
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
#

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
#
# 출력
# 총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
st = []
rst = [-1] * n
for i in range(n):
    # st에 뭔가 있거나 st의 맨윗값이 현재값보다 작을때
    while st and st[-1][0] < arr[i]:
        # st의 맨 윗값을 뽑고 그 인덱스 값을 idx에 넣고
        idx = st.pop()[1]
        # 결과리스트의 idx 자리에 현재값을 넣어주자
        rst[idx] = arr[i]
    # 끝나면 현재값 st에 넣자
    st.append((arr[i], i))
print(*rst)

