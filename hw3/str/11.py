str1 = str(input())
str2 = ""
for i in range(len(str1)):
    if i % 2 == 0:
        str2 += str1[i]
    else:
        str3 = str1.replace(str1[i], "")
        print(str1, str2, str3)