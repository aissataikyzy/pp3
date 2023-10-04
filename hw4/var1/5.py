n = int(input())
# x1, y1, x2, y2 = map(int, input().split())

# print("(", a, ",)")
for i in range(n):
    x1, y1, x2, y2, *trash = map(int, input().split())
    print(*trash)
    a = (y2 - y1) / (x2 - x1)
    b = y1- x1 * a
    print((a, b))