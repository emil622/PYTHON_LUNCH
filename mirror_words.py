import sys
#-------------------------------------------------------------------------------
# Name:        mirror_words.py
# Purpose:     Exercise
#              writes a given word reversed.
#
# Author:      E.M.
#
# Created:     23.03.2012
# Copyright:   (c) emilutz09@gmail.com 2012
# Version      1.0
# Licence:     GPL
#-------------------------------------------------------------------------------
#P\Informatica\GITHUB\PYTHON_LUNCH
__author__ = 'E.M.'
word=sys.argv[1]
print(word[::-1]) #prints the sequence word (all of it specified by first ':')
                    #and :-1 means that it starts from the end of it :)