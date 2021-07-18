N = int(input())

for i in range(N):
    mapp = list(input())
    while len(mapp) != 0:
        if mapp[0] == ')':
            print('NO')
            break
        else:
            if ')' in mapp:
                mapp.remove(')')
                mapp.remove('(')
            else:
                print('NO')
                break
    if len(mapp) == 0:
        print('YES')