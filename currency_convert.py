import sys

__author__ = 'E.M.'
e2u = 1.32
e2j = 109.5
u2j = 82.1
value = 1                        #int(sys.argv[1])
fromm = 'Jpy'                          #sys.argv[2]
toconvert = 'Eur'                           #sys.argv[4]
def converter1(type,rate):
    print ("%.4f" % (type*rate))
def converter2(type,rate):
    print ("%.4f" % (type/rate))
if fromm == 'Eur' and toconvert == 'Usd':
    converter1(value, e2u)
if fromm == 'Eur' and toconvert == 'Jpy':
    converter1(value, e2j)
if fromm == 'Usd' and toconvert == 'Jpy':
    converter1(value, u2j)
if fromm == 'Usd' and toconvert == 'Eur':
    converter2(value, e2u)
if fromm == 'Jpy' and toconvert == 'Eur':
    converter2(value, e2j)
if fromm == 'Jpy' and toconvert == 'Usd':
    converter2(value, u2j)


    #rounded to 4 digits because of the low rate of Jpy
    #1 Jpy is 0.0091 and with 2 digits it would print 0.0