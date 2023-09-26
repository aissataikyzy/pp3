str1 = str(input())
if len(str1) > 3:
    if str1[-3:] == 'ing':
        str1 += 'ly'
        print(str1)
    else:
        str1 += 'ing'
        print(str1)
else:
    print(str1)

