a = int(input())
b = []
while a // 10 >= 1:
    b.append(a % 10)
    a //= 10
b.append(a)
print(b)
c = ""
for i in b:
    c = chr(i+ord("0")) + c

print(c)
print(type(c))
