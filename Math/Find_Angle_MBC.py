# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

angle_ABC = str(round(math.degrees(math.atan(AB / BC)))) + u'\N{DEGREE SIGN}'

print(angle_ABC)
