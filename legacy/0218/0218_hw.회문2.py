import sys
sys.stdin = open("input (hw).txt")

def pal(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-i-1]:
            return False
    return True

t = 10
for tc in range(1, t+1):
    tn = int(input())
    arr = [input() for _ in range(100)]
    # print(tn, arr)
    arr2 = []
    for i in range(100):
        tmp = ""
        # 세로 -> 가로배열로
        for j in range(100):
            tmp += arr[j][i]
        arr2.append(tmp)

    # print(tn, arr2)

    rst = 0
    # 길이 긴거부터
    for i in range(100, -1, -1):
        # 의미 없어짐
        if rst >= i:
            break
        for j in range(100):
            if rst == i:
                break
            for k in range(100-i+1):
                if pal(arr[j][k: k+i]) or pal(arr2[j][k: k+i]):
                    rst = i
                    break

    print('#{} {}'.format(tc, rst))


    # n = 100
    # rst = ""
    # for i in range(n):
    #     for j in range(n - m + 1):
    #         row, r_row = [], []
    #         col, r_col = [], []
    #
    #         for k in range(j, j + m):
    #             row.append(arr[i][k])
    #             col.append(arr[k][i])
    #         for q in range(j + m - 1, j - 1, -1):
    #             r_row.append(arr[i][q])
    #             r_col.append(arr[q][i])
    #         if row == r_row:
    #             for chr in row:
    #                 rst += chr
    #             break
    #         if col == r_col:
    #             for char in col:
    #                 rst += char
    #             break

    # print('#{} {}'.format(tc, rst))





















#
#     # print(arr)
#     rst = 1
#     for i in range(len(arr)):
#         tmp = []
#         tmp_c = []
#         for j in range(len(arr[i])):
#             tmp.append(arr[i][j])
#             tmp_c.append(arr[j][i])
#             if tmp == tmp[::-1]:
#                 if rst <= len(tmp):
#                     rst = len(tmp)
#             if tmp_c == tmp_c[::-1]:
#                 # a.append(len(tmp_c))
#                 if rst <= len(tmp_c):
#                     rst = len(tmp_c)
#     check(map_list2[i][j:j + t_len])
#
#     print('#{} {}'.format(tn, rst))
# def check(a):
#     l = len(a)
#     for i in range(l // 2):
#         if a[i] != a[l - i - 1]:
#             return False
#     return True
#
#
# T = 10
# for t in range(1, T + 1):
#     input()
#     map_list = []
#     map_list2 = []
#     for i in range(100):
#         map_list.append(input())
#     for i in range(100):
#         str_temp = ''
#         for k in range(100):
#             str_temp += map_list[k][i]
#         map_list2.append(str_temp)
#     result = 0
#     for t_len in range(100, 0, -1):
#         if result >= t_len:
#             break
#         for i in range(100):
#             if result == t_len:
#                 break
#             for j in range(100 - t_len + 1):
#                 if check(map_list[i][j:j + t_len]) or check(map_list2[i][j:j + t_len]):
#                     result = t_len
#                     break
#
#     print("#{} {}".format(t, result))