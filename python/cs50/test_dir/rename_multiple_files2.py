import os
import sys
import os
from natsort import natsorted

os.chdir(sys.argv[1])
print(os.getcwd())


counter=1
for f in natsorted(os.listdir()):
    fname, ext= os.path.splitext(f)

    inp = sys.argv[2]
   
    fname= "{}-{}{}".format(inp,counter, ext)
    counter +=1
    print(fname)

    os.rename(f, fname,)
