a = (input().split(",")) #input the array
b = int(input())

c = 0
for i in a:
    if int(i) == b:
        c =+ 1

if c >= 1:
    print('True')
else:
    print("False")
