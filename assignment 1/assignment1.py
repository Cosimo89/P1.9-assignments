from numpy import *
from pylab import *

Input=input("Please select a function: \n 1: x \n 2: sin(x) \n 3: cos(x) \n 4: tan(x) ")

xval=arange(-5.0,5.0,0.1)


if Input == 1:
    yval=xval 
if Input == 2:
    yval=sin(xval)
if Input == 3:
    yval=cos(xval)
if Input == 4:
    yval=tan(xval)

plot (xval,yval, 'b')
show()


