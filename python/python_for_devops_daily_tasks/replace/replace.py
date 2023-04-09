
n = input("")

chars = " #'"
chars2 = ":?!,$&"

for i in chars:
    n= n.replace(i, "-").lower()
for i in chars2:
    n=n.replace(i,"").lower()
print(n)





