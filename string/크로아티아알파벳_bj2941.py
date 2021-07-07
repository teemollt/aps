# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
ca = ["dz=", "z=", "c=", "c-", "d-", "lj", "nj", "s="]
s = input()
for i in ca:
    if i in s:
        s = s.replace(i, "1")
print(len(s))
