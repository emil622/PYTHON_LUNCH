#-------------------------------------------------
# Name:     String-2.py
# Version   V1.0
# Python    V3.2
# Purpose   Learning
#           Enhance python skills
# Author    E.M.
# Created   16.04.2012
# Copyright (c) emilutz09@gmail.com 2012
# Github    https://emil622@github.com/emil622/PYTHON_LUNCH.git
#-----------------------------------------------
#___________________________________________________________________________

'''Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree' '''


def double_char(str):
    result = ''
    for ch in str:
        result += 2*ch
    return result

#___________________________________________________________________________


'''Return the number of times that the string "hi" appears anywhere in the
given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2'''


def count_hi(str):

    return str.count('hi')


#________________________________________________________________________

'''Return True if the string "cat" and "dog" appear the same number of times in
the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True'''


def cat_dog(str):
    return str.count('cat') == str.count('dog')

#_________________________________________________________________________

'''Return the number of times that the string "code" appears anywhere in the
given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2'''

def count_code(str):
    result = 0
    for i in range(0, len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            result += 1
    return result


#_____________________________________________________________________________

'''Given two strings, return True if either of the strings appears at the very
end of the other string, ignoring upper/lower case differences (in other words,
the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True'''


#My solution

def end_other(a, b):
    new_a = a.lower()
    new_b = b.lower()
    if len(a) < len(b):
        return new_a == new_b[-len(a):]
    else:
        return new_b == new_a[-len(b):]

    #Their solution:

    def end_other(a, b):
     a = a.lower()
     b = b.lower()
     return (b.endswith(a) or a.endswith(b))


#______________________________________________________________________________

'''Return True if the given string contains an appearance of "xyz" where the
xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True'''

def xyz_there(str):
    if '.xyz' in str and (str.count('.xyz') == str.count('xyz')):
        return not '.xyz' in str
    else:
        return 'xyz' in str
