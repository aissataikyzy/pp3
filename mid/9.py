import re

text = "Привет, напиши мне на email: user@example.com или user2@gmail.com."
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
email_addresses = re.findall(email_pattern, text)

print("Найденные адреса:")
for email in email_addresses:
    print(email)