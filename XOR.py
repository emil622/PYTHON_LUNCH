__author__ = 'Emil'


# the algorith ia very likely like yours

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


