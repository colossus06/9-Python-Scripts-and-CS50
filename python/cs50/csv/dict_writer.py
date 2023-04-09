import sys
import csv


with open(sys.argv[1]) as f:
    reader=csv.DictReader(f)
    # now every line is a dictionary of coloumns

    with open(sys.argv[2], 'w') as n:
        fieldnames=['first', 'last', 'house']
        writer= csv.DictWriter(n, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            lastn, firstn = row["name"].split(",")
            writer.writerow({"first": firstn.lstrip(), "last": lastn, "house": row["house"] })