import sys

__author__ = 'Emil'
char = sys.argv[1]
depth = int(sys.argv[2])
draw_line = ''
for k in range(1, depth):
    draw_line = draw_line + ' '   # initialing the line with empty space
for i in range(0, depth):
    draw_line = draw_line[1:]     # deleting the first space of the line
    draw_line = draw_line + ' ' + char      #adding a new space between the previous char and the new added one
    print (draw_line)                   #printing the line

'''    *
      * *
     * * *
    * * * *
   * * * * *
  * * * * * *
 * * * * * * *
* * * * * * * *  '''