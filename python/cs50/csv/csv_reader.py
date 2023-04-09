import sys
import csv


with open(sys.argv[1]) as f:
    reader=csv.reader(f)
    
    with open(sys.argv[2], "w") as t:
        writer= csv.writer(t)



        for line in reader:
            writer.writerow(line)
