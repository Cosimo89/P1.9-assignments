from numpy import *
from pylab import *

import sys

if len(sys.argv)==1:

    Input=input("Please select a function: \n 1: x ")
else:
    Input=(int)(sys.argv[1])


xval=arange(-5.0,5.0,0.1)


if Input == 1:
    yval=xval 

plot (xval,yval, 'b')
show()


