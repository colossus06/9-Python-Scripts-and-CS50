from datetime import date
import sys
from xml.dom import ValidationErr
import inflect
import re


p = inflect.engine()


def main():
    bdayk = input("Bday?:")

    try:
        y, m, d= life(bdayk)
    except:
        sys.exit("Invalid time format")
    birth=date(int(y), int(m), int(d))
    tod= date.today()
    dif= tod - birth

    minut= dif.days*24*60

    res=p.number_to_words(minut, andword="")
    print (res.capitalize()+ " minutes")


def life(bdayk):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", bdayk):
        y, m, d =bdayk.split("-")
        return y, m, d
    else:
        ValueError("Oooppsss")






if __name__ == "__main__":
    main()
