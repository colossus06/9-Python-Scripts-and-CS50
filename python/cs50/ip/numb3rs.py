import re


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):

    pattern = r"^((25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)$"


    # pattern = r"^((25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9])\.){3}(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9])$"
    match = re.search(pattern, ip)
    return bool(match)
    # return match.group(1)


if __name__ == "__main__":
    main()