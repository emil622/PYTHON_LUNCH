#SAP: add a header

import sys

__author__ = 'E.M.'
value = int(sys.argv[1])  #SAP: for all programs where sys.argv[] input is expected
                            # you should put a sample at the beginning or in the
                            # header with a new category like
                            #
                            # Parameters: 20 Celsius
                            #             !     !
                            #             !     + or Fahrenheit
                            #             + the temperature, can be minus as well
scale = sys.argv[2]
if scale == 'Celsius':
    temp = (9./5)*value+32
    print ("%.1f" % temp)
elif scale == 'Fahrenheit':
    temp = (5./9)*(value-32)
    print ("%.1f" % temp)
else:
    print('wrong arguments!')
    # -10 Fahrenheit => -23.3
    # 22 Celsius => 71.6