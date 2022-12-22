#Find sine and cosine of angles in degrees.
import math

for i in range(0, 345, 15):
    sine = round(math.sin(math.radians(i)),4)
    cosine = round(math.cos(math.radians(i)),4)
    print(i, " --- ", sine, cosine)