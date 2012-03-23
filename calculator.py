#-------------------------------------------------------------------------------
# Name:        calculator.py
# Purpose:     Exercise
#              calculates some basic math operations.
#
# Author:      E.M.
#
# Created:     23.03.2012
# Copyright:   (c) emilutz09@gmail.com 2012
# Version      1.0
# Licence:     GPL
#-------------------------------------------------------------------------------
#P\Informatica\GITHUB\PYTHON_LUNCH
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
