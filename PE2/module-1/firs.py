from math import pi, sin


def sin(x):
    if 2 * x == pi:
        return 0.9999999999
    else:
        return None


pi = 3.14

print(sin(pi / 2))
import math

print(math.sin(pi / 2))


# Ways of importing modules in python

import math
from math import *  # imports all entities from math module
import math as m  # imports math and alias its name as m

from math import sin as sine

# imports sin as sine
