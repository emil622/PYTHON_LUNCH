__author__ = 'ME'




import sys

# un pic am complicat...
#x = input('give the number: ') #the number can be bin,dec or hex, you take here into account only dec...
x=sys.argv[1]

def print_your_number(num):
    print ('your number is: ' + x )

def dec2bin(num):
    print ('the binary form of ', num, ' is: ',  bin(num))

def bin2dec(num):
    print ('the decimal number of ', num, ' is: ', int(str(num),2)) # convert to upper

def dec2hex(num):
    print ('the hexadecimal number of ',num, ' is: ', str((hex(num))).upper()) # convert to upper

def hex2dec(num):
    print ('the decimal number of ', num, ' is: ', int(num)) # convert to upper

def hex2bin(num):
    print ('the binary form of ',num, 'is: ',  bin(int(str(num))))

def bin2hex(num):
    print ('the hexadecimal form of ', num, 'is: ',  hex(int(str(num),2)))


num = (x[1:])
print_your_number(num) # print user number
number_base = x[0]

if number_base == 'h':
    hex2bin(int(num,16))
    hex2dec(int(num,16))

elif number_base == 'b':
    bin2hex(int(num))
    bin2dec(int(num))
else:
    dec2hex(int(num))
    dec2bin(int(num))
