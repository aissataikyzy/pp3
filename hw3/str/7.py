str1 = str(input("Sample String :"))

if str1.find('poor') > str1.find('not') and str1.find('not')>0 and str1.find('poor')>0:
    str1 = str1.replace(str1[str1.find('not'):(str1.find('poor')+4)], 'good')
    print(str1)
