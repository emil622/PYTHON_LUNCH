import sys
#SAP: add a header

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
elif fromm == 'Eur' and toconvert == 'Jpy':
    converter1(value, e2j)
elif fromm == 'Usd' and toconvert == 'Jpy':
    converter1(value, u2j)
elif fromm == 'Usd' and toconvert == 'Eur':
    converter2(value, e2u)
elif fromm == 'Jpy' and toconvert == 'Eur':
    converter2(value, e2j)
elif fromm == 'Jpy' and toconvert == 'Usd':
    converter2(value, u2j)
else:
    print ('wrong arguments!')


    #rounded to 4 digits because of the low rate of Jpy
    # 1 Jpy is 0.0091 Eur and with 1 digit it would print 0.0