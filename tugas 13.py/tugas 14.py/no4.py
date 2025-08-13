# List awal
a = [1, 2, 3, 4, 5]

# b alias a (nunjuk ke list yang sama)
b = a

# c adalah salinan dari a (list baru)
c = a.copy()
b[1] = 20
c[1] = 30

# print

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
