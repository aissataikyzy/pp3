a = input().split()
b = input().split()

c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)

y = set(c)
u = list(y)
u.sort()
print(u)