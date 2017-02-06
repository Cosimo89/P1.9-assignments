from numpy import *
from pylab import *

import sys

if len(sys.argv)==1:

    Input=input("Please select a function: \n 1: x \n 2: exp(x) \n 3: sqrt(x) \n")
else:
    Input=(int)(sys.argv[1])


xval=arange(-5.0,5.0,0.1)


if Input == 1:
    yval=xval 
if Input == 2:
    yval=exp(xval)
if Input == 3:
    yval=sqrt(xval)

plot (xval,yval, 'b')
show()


