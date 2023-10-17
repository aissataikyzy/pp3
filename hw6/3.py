import re
n = int(input())
reg = r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
val_em = []
for i in range(n):
    email = input().strip()
    if re.match(reg, email):
        val_em.append(email)

val_em.sort()
for email in val_em:
    print(list(email))