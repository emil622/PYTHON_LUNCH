__author__ = 'E.M.'


#-------------------------------------------------------------------------------
# Name:        XOR.py
# Purpose:     Exercise
#              encrypts texts.
#
# Author:      E.M.
#
# Created:     23.03.2012
# Copyright:   (c) emilutz09@gmail.com 2012
# Version      1.0
# Licence:     GPL
#-------------------------------------------------------------------------------
#P\Informatica\GITHUB\PYTHON_LUNCH

def cryptXOR(s, key="Python"):
    output = ""
    for character in s:
        for letter in key:
            character = chr(ord(character) ^ ord(letter))
        output += character
    return output

s = cryptXOR('mQU\\\x1a\x14S[\x14@[\x14GXQQD\x14Z[C\x15')
print repr(s)
print repr(cryptXOR(s))


