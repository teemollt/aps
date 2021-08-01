# 자연수 과 정수 가 주어졌을 때 이항 계수
# 를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
# def fac(n):
#     if n == 1:
#         return 1
#     return fac(n-1)*n
#
n, k = map(int, input().split())
#
# rst = (fac(n) / (fac(k) * fac(n-k))) % 1000000007
# print(rst)
def fac(n):
    if n == 1:
        return 1
    return fac(n-1)