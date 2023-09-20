print("Input lengths of the triangle sides:")
x = input("x: ")
y = input("y: ")
z = input("z: ")
if(x == y and x == z):
    print("Equilateral triangle")
elif(x == y or x == z or y == z):
    print("Isosceles triangle")
else:
    print("Scalene triangle")