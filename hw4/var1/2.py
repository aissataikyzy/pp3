def move(s):
    if not s:
        return s

    a = s[-1]
    for i in range(len(s) - 1, 0, -1):
        s[i] = s[i - 1]
    s[0] = a

s = [1, 2, 3, 4, 5]
move(s)
print(s)