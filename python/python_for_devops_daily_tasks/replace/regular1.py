import re

email= input("Enter an email:")


match = re.search(r"^[^@]+@[^@]+\.edu$", email)

if match:
    print("Found", match.group())
else:
    print("Ooops")