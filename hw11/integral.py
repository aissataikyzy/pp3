import math

n = 50
s = 0

for a in range(1, n + 1):
    for b in range(a, n + 1):
        c_squared = a**2 + b**2
        c = int(math.sqrt(c_squared))
        
        if a + b > c and 2 * (a**2) + 2 * (b**2) > c_squared:
            m = math.sqrt(2 * (a**2) + 2 * (b**2) - c_squared) / 2
            if m.is_integer():
                s += 1
                print(a, b, c, m)

print(s)
