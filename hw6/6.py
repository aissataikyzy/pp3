import re

# Regular expression pattern to match valid email addresses
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$'

n = int(input())

l = []

for _ in range(n):
    line = input().strip()
    name, email = line.split('<')
    email = email.rstrip('>').strip()

    if re.match(email_pattern, email):
        l.append((name.strip(), email))

for name, email in l:
    print(f"{name} <{email}>")
