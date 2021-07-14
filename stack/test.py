n = int(input())
a = list(map(int, input().split()))
c=1
s=[]
r=""
for i in a:
    while c<=i:
        s+=[c]
        c+=1
        r+="+\n"
    if s[-1]==i:
        s.pop()
        r+="-\n"
    else:r="NO";break
print(r)