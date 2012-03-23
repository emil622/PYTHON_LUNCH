#SAP: add a header


import sys
import random
import os
'''
__author__ = 'E.M.'

n = int(sys.argv[1])
range = int(sys.argv[2])  #read the range of randomized numbers, you get a string, but later u need as integer
filename = sys.argv[3]     #reading the file name

f = open(filename, 'a') # vezi modus... a=apend

#print(n) # asa primesti parametri, intelegi?
f.write('This is a random generated number list created with ' + sys.argv[0])
'''

'''
for i in range(0,n):
    #f.write(str(random.randint(1, range)))
    print('test')

for i in range(0,10):
    f.write(random.randint(1, range))

'''


def my_help():
    print(''' asdfsdf
              sdfg
              asdasdfsdf sda
              asdfasdfasdf
              s ''')

#get user input
print(sys.argv[0])
n = int(sys.argv[1])
m = int(sys.argv[2])
filename = sys.argv[3]




my_help()

f = open(filename,'a') ## f.seek()

# generate random numbers
for i in range(0,n):
    f.write('\n' + str(random.randint(0,m)))
    print ('\t' + str(random.randint(0,m)))
    f.write('\t' + str(random.uniform(1, m)))




