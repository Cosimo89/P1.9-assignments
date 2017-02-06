from numpy import *
from pylab import *
import sys

if len(sys.argv)==1:

    Input=input("Please select a function: \n 1: x \n 2: x**2\n 3: x**3\n 4: sin(x) \n 5: cos(x) \n 6: tan(x) ")

else:
    Input=(int)(sys.argv[1])




xval=arange(-3.0,3.0,0.1)



if Input == 1:
    yval=xval 
if Input == 2:
    yval=xval**2 
if Input == 3:
    yval=xval**3 
if Input == 4:
    yval=sin(xval)
if Input == 5:
    yval=cos(xval)
if Input == 6:
    yval=tan(xval)


plot (xval,yval, 'b')
show()


