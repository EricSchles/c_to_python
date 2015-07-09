import struct
import numpy as np
things = []
# source: http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
dt = np.dtype([('float',np.float64,),('int',np.int_),('char',np.chararray),('char1',np.str_),('char2',np.str_),('char3',np.str_)])
with open("output.bin","rb") as f:
    chunk = f.read(16)
    while chunk != "":
        print len(chunk)
        #the string is a set of format characters
        #more details at: https://docs.python.org/2/library/struct.html
        things.append(np.array(struct.unpack('dissss', chunk),dtype=dt))
        chunk = f.read(16)
print things
