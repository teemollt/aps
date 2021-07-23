# def sol(a, b, c, s):
#     if s == b:
#         rst = a % c
#
#     elif s < b and 2*s <= b:
#         a = a*a
#         s = s*2
#         sol(a,b,c,s)
#     else:
#         for i in range(c-s):
#             a = a*oa
#             s += 1
#         if s == b:
#             rst = a % c
#
#
# a, b, c = map(int, input().split())
# # for i in range(b):
# #     a *= a
# # print(a%c)
# # 당연히 시간초과
# oa = a
# sol(a,b,c,1)
# print(a)
