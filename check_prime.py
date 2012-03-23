#-------------------------------------------------------------------------------
# Name:        check_prime.py
# Purpose:     Demo
#              Check if a given number is prime.
#
# Author:      E.M.
#
# Created:     23.03.2012
# Copyright:   (c) 541840@gmail.com 2012
# Version      1.0
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import sys

__author__ = 'E.M.'
num = 11 #int(sys.argv[1])
validator = 1
for i in range(2, num/2):  #it checks if the modulus of number with al numbers within the range (2, number/2) is 0
    if num % i == 0:     #if it is 0 then the number is prime, else isn't
        validator = 0
if validator == 1:
    print (repr(num) + ' True')
else:
    print (repr(num) + ' False')
