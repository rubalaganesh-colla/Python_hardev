import math 
print('the value of pi is :',math.pi)
str(math.ceil(5.5)) +', ' + str(math.floor(5.5))
x= int(input('enter a number:'))
y= int(input('enter another number:'))
print('the value of x after coping the sign from y is: ' +str(math.copysign(x,y)))
print('the value of x after rounding to the nearest integer is: ' +str(math.trunc(x)))
print('the value of x after calculating the square root is: ' +str(math.sqrt(x)))