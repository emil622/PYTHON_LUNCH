
#SAP: add a header
import sys

__author__ = 'E.M.'

num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
operator = '-'      #sys.argv[2]

if operator == '+':
    print (num1+num2)
elif operator == '-':
    print (num1-num2)
elif operator == '/':
    print (num1/num2)
elif operator == '*':
    print (num1*num2)
else:
    print ('wrong arguments!!')
