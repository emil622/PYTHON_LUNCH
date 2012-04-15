#-------------------------------------------------
# Name:     String-1.py
# Version   V1.0
# Python    V3.2
# Purpose   Learning
#           Enhance python skills
# Author    E.M.
# Created   15.04.2012
# Copyright (c) emilutz09@gmail.com 2012
# Github    https://emil622@github.com/emil622/PYTHON_LUNCH.git
#-----------------------------------------------

#___________________________________________________________________

'''Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!' '''


def hello_name(name):

    return 'Hello ' + name + '!'


#___________________________________________________________________


'''Given two strings, a and b, return the result of putting them together in
the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('x', 'y') → 'xyyx' '''


def make_abba(a, b):
    return a + 2*b +a


#_____________________________________________________________________


'''The web is built with HTML strings like "<i>Yay</i>" which draws Yay as
italic text. In this example, the "i" tag makes <i> and </i> which surround
the word "Yay". Given tag and word strings, create the HTML string with tags
around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>' '''



def make_tags(tag, word):

    return '<%s>%s</%s>' % (tag, word, tag)



#________________________________________________________________________

'''Given an "out" string length 4, such as "<<>>", and a word, return a new
string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]' '''



def make_out_word(out, word):

    return out[0:2] + word + out[2:]

#___________________________________________________________________________


'''Given a string, return a new string made of 3 copies of the last 2 chars of
the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi' '''


def extra_end(str):

    return 3*str[-2:]


#____________________________________________________________________________


'''Given a string, return the string made of its first two chars, so the
String "Hello" yields "He". If the string is shorter than length 2, return
whatever there is, so "X" yields "X", and the empty string "" yields the empty
string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab' '''



def first_two(str):

    return str[0:2]


#____________________________________________________________________________

'''Given a string of even length, return the first half. So the string
"WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc' '''



def first_half(str):

    return str[0:len(str)/2]


#_________________________________________________________________________

'''Given a string, return a version without the first and last char, so
"Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin' '''



def without_end(str):

    return str[1:len(str)-1]

#_____________________________________________________________________

'''Given 2 strings, a and b, return a string of the form short+long+short,
 with the shorter string on the outside and the longer string on the inside.
 The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab' '''


def combo_string(a, b):

    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


#________________________________________________________________________

'''Given 2 strings, return their concatenation, except omit the first char
of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava' '''


def non_start(a, b):

    return a[1:] + b[1:]

#________________________________________________________________________


'''Given a string, return a "rotated left 2" version where the first 2 chars
are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi' '''


def left2(str):

    return str[2:] + str[0:2]