import sys

__author__ = 'E.M.'
value = int(sys.argv[1])
scale = sys.argv[2]
if scale == 'Celsius':
    temp = (9./5)*value+32
    print ("%.1f" % temp)
elif scale == 'Fahrenheit':
    temp = (5./9)*(value-32)
    print ("%.1f" % temp)

    # -10 Fahrenheit => -23.3
    # 22 Celsius => 71.6