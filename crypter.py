import sys

__author__ = 'E.M.'
#def lungime(chara):
 #   if len(chara) < 7 :
  #      while len(chara) < 7:
   #         chara.insert(0,'0')
'''
key = sys.argv[1] #input('your key is: ') # sorry, this is also ok
message = sys.argv[2] #input('your message is: ')
#message = 'dPTD@\SYRJ^G[S_JZM\@FZFWGLYUYTJKTWV'
message="test"
k = 0
crypt = ''

for i in message:

    crypt = chr(ord("k")^ord(i))

    if k == len(key)-1:
        k = 0
    else:
        k += 1

    print (ord(crypt))
'''
from itertools import izip, cycle

def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

my_data = "mQU\\\x1a\x14S[\x14@[\x14GXQQD\x14Z[C\x15"
my_key= "Python"

# problma e k nu sunt aratate caracterele non-alpha numerice.



# Do the actual encryption
encrypted = xor_crypt_string(my_data, key=my_key)
print repr(encrypted)

# This will obtain the original data from the encrypted
original = xor_crypt_string(encrypted, key=my_key)
print repr(original)