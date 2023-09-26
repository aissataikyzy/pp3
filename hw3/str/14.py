str1 = input("Input comma separated sequence of words") # dog,cat,dog,bird
words = sorted(set(str1.split(',')))
print (words)