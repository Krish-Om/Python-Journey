import math
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.__x = (x)
        self.__y =(y)


    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def distance_from_xy(self,x,y):
        return math.hypot(self.__x,self.__y)
    
    def distance_from_point(self,point):
        resX = math.sqrt((self.__x**2)+(point.getX()**2))
        resY = math.sqrt((self.__y**2)+(point.getY()**2))

        return math.hypot(resX,resY)
    
if __name__ == "__main__": #this makes sures that, this script is not executed when imported by other script
    print("Executing this script file: ",__name__ + ".py")
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))