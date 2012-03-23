import sys
#-------------------------------------------------------------------------------
# Name:        Pascal_triangle_symbolic.py
# Purpose:     Exercise
#              Writes Pascal's triangle.
#
# Author:      E.M.
#
# Created:     23.03.2012
# Copyright:   (c) emilutz09@gmail.com 2012
# Version      1.0
# Licence:     GPL
#-------------------------------------------------------------------------------
#P\Informatica\GITHUB\PYTHON_LUNCH

__author__ = 'Emil'
char = sys.argv[1]
depth = int(sys.argv[2])
draw_line = ''
for k in range(1, depth):
    draw_line = draw_line + ' '   # initialing the line with empty space
for i in range(0, depth):
    draw_line = draw_line[1:]     # deleting the first empty space of the line, [:1] means everything starting from the second element
    draw_line = draw_line + ' ' + char      #adding a new space between the last char of the line and the new added one
    print (draw_line)                   #printing the line

'''    *
      * *
     * * *
    * * * *
   * * * * *
  * * * * * *
 * * * * * * *
* * * * * * * *  '''