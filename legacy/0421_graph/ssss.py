a = [(1,2), (4, 1), (39, 12), (1,4), (40, 1)]

print(a)
a.sort(key=lambda x: x[0])
print(a)