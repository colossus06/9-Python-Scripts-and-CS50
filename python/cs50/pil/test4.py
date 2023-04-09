import sys


s= input("Enter")

result = s[s.find("(")+1:s.find(")")]

print(result)
