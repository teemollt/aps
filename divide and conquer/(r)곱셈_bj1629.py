def sol(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (sol(a, b // 2, c) ** 2) % c
    else:
        return ((sol(a, b // 2, c) ** 2) * a) % c


a, b, c = map(int, input().split())
print(sol(a, b, c))


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
# 재귀로 제곱하면서 몇제곱인지와 결과값을 계속 같이 리스트에 넣어준다
# s 몇제곱인지?
# def sol(a,b,c,s):
#     global v
#     if s == b:
#         print(a % c)
#     elif s < b and s*2 <= b:
#             s *= 2
#             a *= a
#             v.append((s, a))
#             return sol(a,b,c,s)
#     else:
#         for i in range(len(v)-1, -1, -1):
#             if s + v[i][0] <= b:
#                 while s + v[i][0] <= b:
#                     a *= v[i][1]
#                     s += v[i][0]
#                     return sol(a,b,c,s)
#
#
#
# # a를 b번 곱한수를 c로 나눈 나머지

# v = [(1, a)]
# sol(a,b,c,1)

# print(pow(a,b,c))
# def sol(a, b, c, s):
#     global v
#     if s == b:
#         print(a % c)
#         return
#     v.append((a, s))
#     if 2*s <= b:
#         return sol(a*a, b, c, s*2)
#     else:
#         idx = len(v)-1
#         while v[idx][1] + s > b:
#             idx -= 1
#         v = v[:idx+1]
#         return sol(a*v[idx][0], b, c, s+v[idx][1])
