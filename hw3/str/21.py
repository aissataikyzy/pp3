str1 = str(input())
str2 = '''Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.'''
a = str2.split("\n")
for i in range(len(a)):
    s = str1 + a[i]
    print(s)
# print(a)