str1 = str(input())
str2 = str(input())
new_str1 = str2[:1] + str1[1:]
new_str2 = str1[:1] + str2[1:]
print(new_str1 + ' ' + new_str2) 