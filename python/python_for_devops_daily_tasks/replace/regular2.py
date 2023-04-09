import re

# \w means elphanumeric 0-9 , a-zA-Z and _

email = input("Enter your email: ").strip()

# alphabetical or numerical = alphanumeric

match = re.search(r"^\w+@\w+\.(com|edu)$", email)

if match:
    print("Yep, found", match.group())
else:
    print("Ooopsssss.....")