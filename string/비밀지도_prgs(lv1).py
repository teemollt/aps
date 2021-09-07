def tob(num, n):
    rst = ''
    while num > 0:
        rst = str(num % 2) + rst
        num //= 2
    if len(rst) < n:
        rst = '0' * (n - len(rst)) + rst
    return rst

def solution(n, arr1, arr2):
    arr = ["" for _ in range(n)]
    for i in range(n):
        arr1[i] = tob(arr1[i], n)
        arr2[i] = tob(arr2[i], n)
        for j in range(n):
            if int(arr1[i][j]) or int(arr2[i][j]):
                arr[i] += "#"
            else:
                arr[i] += " "
    return arr