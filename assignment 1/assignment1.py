from numpy import *
from pylab import *

Input=input("Please select a function: \n 1: x \n 2: x**2 \n 3: x**3 \n")

xval=arange(-5.0,5.0,0.1)


if Input == 1:
    yval=xval 
if Input == 2:
    yval=xval**2
if Input == 3:
    yval=xval**3

plot (xval,yval, 'b')
show()


