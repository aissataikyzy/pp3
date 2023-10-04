n = int(input())
a = input().split()
b = sorted(a)
for i in b:
    print(a.index(i) + 1)