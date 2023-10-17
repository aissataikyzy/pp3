#import re
#text = str(input())
#x = re.sub("&&", "and", text)
#y = re.sub("||", "or", text)
#print(y)

n = int(input())
line = []
for i in range(n):
    l = input()
    new_line = l.replace("&&", "and").replace("||", "or")
    line.append(new_line)

for l in line:
    print(l)