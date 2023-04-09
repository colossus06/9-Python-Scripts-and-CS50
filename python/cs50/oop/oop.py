class Student():
    def __init__(self,name,house):
        self.name=name
        self.house=house

   

def main():
    student=get_student()
    print(student["name"])



def get_student():
    student= {}
    name =input("name: ")
    last=input("last: ")
    return {"name": name, "last": last}

if __name__ =="__main__":
    main()