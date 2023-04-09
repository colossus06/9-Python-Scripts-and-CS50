from ast import Continue
from multiprocessing.sharedctypes import Value
import re
import sys


def main():
    print(convert(input("Hours: ")))
# x  y  z  k t w  p
# 9:00 AM to 5:00 PM
# 9 AM to 5:30 PM
# 9 AM to 5 PM


def convert(s):

    pattern = r'([1-9]|1[0-2])(?:(\:[0-5][0-9]\s| ))(AM|PM)\s(\w+)\s([1-9]|1[0-2])(?:(\:[0-5][0-9]\s| ))(AM|PM)'
    # ([1-9]|1[0-2])( |:\s([0-5][0-9])?) ===== cathes both 5: and 5
    if match := re.search(pattern, s):
        x, y, z, k, t, w, p = match.groups()

        # return match.groups()
        print(f"{x}{y}{z} {k} {t}{w}{p}")
        print(type(int(x)))

        if z == "PM" and p == "AM":
            x = int(x)-12
            if y == " " and w == " ":
                return f"{x:02}:00 {k} {t}:00"
            elif y == " " and w != " ":
                return f"{x}0:00 {k} {t}{w}"
            elif y != " " and w != " ":
                return f"{x:02}{y}{k} {t}{w}"
            elif y != " " and w == " ":
                return f"{x:02}{y}{k} {t}:00"
# x  y  z  k t w  p
# 9:00 AM to 5:00 PM
# 9 AM to 5:30 PM
# 9 AM to 5 PM

        elif z == "PM" and p == "PM":
            if x and t == "12":
                x = int(x)-12
                t = int(t)-12
                if y == " " and w == " ":
                    if x and t=="12":
                        return f"{x:02}:00 {k} {t:02}:00"
                    else:
                        return f"{x}:00 {k} {t}:00"
                elif y == " " and w != " ":
                    return f"{x}0:00 {k} {t}{w}"
                elif y != " " and w != " ":
                    return f"{x:02}{y}{k} {t:02}{w}"
                elif y != " " and w == " ":
                    return f"{x:02}{y}{k} {t}:00"

    else:
        print("value error")


if __name__ == "__main__":
    main()
