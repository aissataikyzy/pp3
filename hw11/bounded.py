import math

n=5
l=[[2]]

def func():
    l1=l.copy()
    l.clear()
    i=len(l1[0])
    j=i+1
    for a in l1:
        xi=a[i-1]
        xj1=math.floor(xi**(j/i)-1)+1
        xj2=math.ceil((xi+1)**(j/i))-1
        for b in range(xj1,xj2+1,1):
            a1=a.copy()
            a1.append(b)
            l.append(a1)

    return l

for _ in range(n-1):
    func()

print(len(l))                                          #заключительное решение