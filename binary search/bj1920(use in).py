import sys
n = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
for i in x_list:
    if i in arr:
        print(1)
    else:
        print(0)