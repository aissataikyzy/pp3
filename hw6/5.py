import re
pattern = r'^(\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}|\d{11}|\+\d{10})$'

n = int(input())

results = []

for i in range(n):
    string = input().strip()
    if re.match(pattern, string):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)
