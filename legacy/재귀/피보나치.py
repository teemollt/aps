def fc(num):
    if num > 1:
        return num * fc(num - 1)
    else:
        return 1
n = int(input())
print(fc(n))