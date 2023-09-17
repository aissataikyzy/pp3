n = " "
for i in range(0, 4):
    if i in range(1, 4):
        n = n + "*"

    for j in range(0, 7):
        if j in range(1,7):
            n = n + "*"


print(n)