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


'''Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13
also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6'''
def sum13(nums):
    sum = 0
    for i in range(0, len(nums)):
        if nums[i] == 13 and i in range (len(nums)-2,len(nums)):
            break
        elif i > 0 and nums[i] != 13 and nums[i-1] != 13:
            sum += nums[i]
        elif nums[i] != 13 and i == 0:
            sum += nums[i]
    return sum      # aghh, finally solved :)) ...This one was tough, not hard but challenging


#________________________________________________________________________________

'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# //SAP try this, don't need to be tooo complicated. think out of the box.
#       except this, you did great, anyway! well done!
def sum67(nums):
   nums=nums[:]
   while 6 in nums:
     i=nums.index(6)
     j=nums.index(7,i)
     del nums[i:j+1]
   return sum(nums)



sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4'''

def sum67(nums):
    sum = 0
    if 7 in nums and 6 in nums:
        poz6 = nums.index(6)
        poz7 = nums.index(7)
        if poz7 < poz6:
            new1 = nums[:poz7] + nums[poz7+1:]
            poz6 = new1.index(6)
            poz7 = new1.index(7)
        if poz6 < poz7:
            new = nums[0:poz6] + nums[poz7+1:]
            if 7 in new and 6 in new:
                poz6 = new.index(6)
                poz7 = new.index(7)
                if poz6 < poz7:
                    new = new[0:poz6] + new[poz7+1:]
        else:
            new = nums
    else:
        new = nums
    for i in new:
        sum += i
    return sum   # This doesn't pas the 'other tests' validation, it was the last problem and i wanted to finish

#_________________________________________________________________________________

'''Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False'''

def has22(nums):
    check = 0
    for i in range(0, len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            check = 1
            break
    return check == 1