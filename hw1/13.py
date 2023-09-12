print("Three coordinates of circle : ")
x1, y1, x2, y2, x3, y3 = map(float, input().split)
a = (x1 - x2)**2 + (y1 - y2)**2
b = (x2 - x3)**2 + (y2 - y3)**2
c = (x3 - x1)**2 + (y3 - y1)**2
S = 2 * (a * b + b * c + a * c) - (a * a + b * b + c * c)
Px = (a * (b + c - a) * x3 + b * (a + c - b) * x2 + c * (a + b - c) * x1) / S
Py = (a * (b + c - a) * y3 + b * (a + c - b) * y2 + c * (a + b - c) * y1) / S
ra = a**0.5
rb = b**0.5
rc = c**0.5 
R = ra * rb * rc / ((ra + rb + rc) * (- ra + rb + rc) * (ra - rb + rc) * (ra + rb - rc))**(1 / 2)
print("Radius :")
print(R)
print("Central coordinate :")
print(Px, Py)
