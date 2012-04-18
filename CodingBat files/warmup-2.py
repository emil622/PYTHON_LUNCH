#-------------------------------------------------
# Name:     Warmup-2.py
# Version   V1.0
# Python    V3.2
# Purpose   Learning
#           Enhance python skills
# Author    E.M.
# Created   15.04.2012
# Copyright (c) emilutz09@gmail.com 2012
# Github    https://emil622@github.com/emil622/PYTHON_LUNCH.git
#-------------------------------------------------

#____________________________________________________________________

'''Given a string and a non-negative int n, return a larger string that is n
copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi' '''


def string_times(str, n):

 return str*n


#__________________________________________________________________________

'''Given a string and a non-negative int n, we'll say that the front of the
string is the first 3 chars, or whatever is there if the string is less than
length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc' '''


def front_times(str, n):

 if len(str) <= 3:
    return str*n
 else:
    return n*str[0:3]


#___________________________________________________________________________


 '''Given a string, return a new string made of every other char starting
 with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello' '''


 def string_bits(str):

  return str[0::2]

#________________________________________________________________________


'''Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab' '''


def string_splosion(str):
    result = ''
    for i in range (1,len(str)+1):
        result = result + str[0:i]
    return result



#______________________________________________________________________


'''Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the string, so
"hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2'''



def last2(str):
    last = str[len(str)-2:]    # slice the last 2 chars
    count = 0
    for i in range (0, len(str)-2):
        if last == str[i:i+2]:
            count += 1                #we increment the counter if last occurs again in the string
    return count


#_____________________________________________________________________

'''Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3'''

def array_count9(nums):

 return nums.count(9)


#____________________________________________________________________


'''Given an array of ints, return True if one of the first 4 elements
in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False'''


def array_front9(nums):

    if len(nums) <=4:
        return 9 in nums
    else:
        return 9 in nums[0:4]


#_________________________________________________________________


    '''Given an array of ints, return True if .. 1, 2, 3, .. appears in the
    array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True'''


def array123(nums):
 for i in range (0, len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
        return True
 return False


#___________________________________________________________________

'''Given 2 strings, a and b, return the number of the positions where they
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0'''


def string_match(a, b):
    count = 0
    l = 0
    if len(a) < len(b):
        l = len(a)
    else:
        l = len(b)
    for i in range (0, l-1):
        if a[i:i+2] == b [i:i+2]:
            count += 1
    return count