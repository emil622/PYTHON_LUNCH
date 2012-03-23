import sys
#SAP: add a header
__author__ = 'E.M.'
#def lungime(chara):
 #   if len(chara) < 7 :
  #      while len(chara) < 7:
   #         chara.insert(0,'0')

key = sys.argv[1] #input('your key is: ')
message = sys.argv[2] #input('your message is: ')
k = 0
crypt = ''
for i in message:
    crypt = crypt.append(key[k]^i)
    if k == len(key)-1:
        k = 0
    else: k += 1
print('your message is: ' + crypt + '     isn\'t?')


