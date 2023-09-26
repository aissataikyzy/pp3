a = input()
lowers = []
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyz":
        lowers.append(i)
print(lowers[0:4])