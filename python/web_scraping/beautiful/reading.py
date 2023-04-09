
with open("demo_list.txt") as f:
    my_lines = f.readlines()
    
   

# data = [
#     "Hello World!",
#     "This is a Python program.",
#     "It will write some data to a file.",
#     "Line by line."
# ]

counter=0

for line in my_lines:
    file = open(f"file.txt{counter}", "w")
    file.write(line + "\n")
    counter+=1
    
#file.close()