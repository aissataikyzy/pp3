def median():
    a=int(input("Input first number:"))
    b=int(input("Input second number:"))
    c=int(input("Input third number:"))
    print("The median is:",end=" ")
    if a>b:
        if a<c:
            print(a)
        elif b>c:
            print(b)
        else:
            print(c)
    else:
        if a>c:
            print(a)
        elif b<c:
            print(b)
        else:
            print(c)