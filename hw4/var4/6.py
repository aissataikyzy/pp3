n=int(input())
s=''
for i in range(n):
    m=input().split()
    a,b,c=[int(i) for i in m]
    c1=(a**2+b**2)**(0.5)
    if c==c1:
        s=s+'R'
    elif c>c1:
        s=s+'O'
    elif c<c1:
        s=s+'A'
print(s)