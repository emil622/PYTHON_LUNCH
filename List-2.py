#-------------------------------------------------
# Name:     List-2.py
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

'''Return the number of even ints in the given array. Note: the % "mod" operator
computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0'''

def count_evens(nums):

    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

#____________________________________________________________________________


'''Given an array length 1 or more of ints, return the difference between the largest and smallest
values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8'''


def big_diff(nums):
    new = sorted(nums)
    return new[-1] - new[0]


#______________________________________________________________________________

'''Return the "centered" average of an array of ints, which we'll say is the mean average of
the values, except not counting the largest and smallest values in the array. Use int division to
produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3'''

def centered_average(nums):
    new = sorted(nums)
    avg = 0
    for i in range(1, len(new)-1):
        avg += new[i]
    return avg/ (len(new)-2)


#_____________________________________________________________________________

