import math

class NewValuError(ValueError):
    def __init__(self, name,color,state):
        self.data=(name,color,state)

try:
    raise NewValuError("Enemey Warning","Red Alet","High readiness")
except NewValuError as nve:
    for arg in nve.args:
        print(arg,end = "! ")
