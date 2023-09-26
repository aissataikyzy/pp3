str1 = str(input())
if len(str1) % 4 == 0:
    print(''.join(reversed(str1)))
else:
    print(str1)