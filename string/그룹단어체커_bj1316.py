# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다
# 한번 나왔던 알파벳이 다른거 나오고 다시 등장하면 탈락
n = int(input())
cnt = 0
for i in range(n):
    w = input()
    idx = 0
    ws = ['1']
    while idx < len(w):
        if ws[-1] != w[idx] and w[idx] in ws:
            break
        elif ws[-1] != w[idx] and w[idx] not in ws:
            ws.append(w[idx])
        idx += 1
    else:
        cnt += 1
print(cnt)