#-------------------------------------------------------------------------------
# Name:        check_prime.py
# Purpose:     Exercise
#              Check if a given number is prime.
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
import time

start_time = time.time()

validator = 1
num = 99999999 #int(sys.argv[1]) # 8 digits is the max num... how can you use greater numbers?
               # Output
               # 99999999 False
               # (0.83500003814697266, 'seconds')
for i in range(2, int((num/2)-1)):  #it checks if the modulus of number with al numbers within the range (2, number/2) is 0
    if num % i == 0:    #if it is 0 then the number is prime, else isn't
        validator = 0
        break
if validator == 1:
    print (repr(num) + ' True')
else:
    print (repr(num) + ' False')

print (time.time() - start_time, 'seconds')