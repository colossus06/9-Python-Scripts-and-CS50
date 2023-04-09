import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 9 AM to 5 PM------ 09:00 to 17:00
    # 9:00 AM to 5:00 PM --------09:00 to 17:00
    # 11:30 PM to 9:59 AM -------23:30 to 09:59

    if match := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE):
        h1, m1, ap1, h2, m2, ap2 = match.groups()
        #return h1, m1, ap1, h2, m2, ap2

        if m1:
            if int(m1) >= 60:
                raise ValueError("fdf")
        if m2:
            if int(m2)>=60:
                raise ValueError("dsfsf")
            # now we've got the minutes value errors

    
        h1 = int(match.group(1))

        if ap1 == "PM" and h1 != 12:
            h1 += 12
        elif ap1 == "AM" and h1 == 12:
            h1 -= 12
        if m1 == None:
            t1 = f"{h1:02}:00"
        else:
            t1 = f"{h1:02}:{m1}"

        print(t1)

        h2 = int(match.group(4))

        if ap2 == "PM" and h2 != 12:
            h2 += 12
        elif ap2 == "AM" and h2 == 12:
            h2 -= 12
        if m2 == None:
            t2 = f"{h2:02}:00"
        else:
            t2 = f"{h2:02}:{m2}"

        time24= f"{t1} to {t2}"
        return time24
    else:
        raise ValueError
    # we've got the format error


if __name__ == "__main__":
    main()
