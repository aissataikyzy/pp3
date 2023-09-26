str1 = str(input())
n = int(input())
try:
    str1=list(str1)
    del str1[n]
    print(''.join(str1))
except:
    print("Error")