from math import pi, radians, degrees, sin, cos, tan, asin, acos, atan

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.0)
print(ar == pi / 2.0)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
