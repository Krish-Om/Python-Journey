import math
from pointsOnPlane import Point

class Triangle:
    def __init__(self,v1,v2,v3):
        self.__coordinate = [v1,v2,v3]

    def perimeter(self):
        per = 0 
        for i in range(3):
            per += self.__coordinate[i].distance_from_point(self.__coordinate[(i+1)%3])
        return per
    
triangle = Triangle(Point(0,0),Point(1,0),Point(1,0))
print(triangle.perimeter())
    