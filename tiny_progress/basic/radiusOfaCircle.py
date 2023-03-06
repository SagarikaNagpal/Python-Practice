# https://www.geeksforgeeks.org/python-program-for-program-to-find-area-of-a-circle/
# The area of a circle can simply be evaluated using the following formula.
#
# Area = pi * r2
# where r is radius of circle

import math
def area(r):
    a = round((math.pi * pow(r,2)),2)
    return a
r = int(input('r: '))
print(area(r))

