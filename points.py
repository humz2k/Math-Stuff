import math
import random
import matplotlib.pyplot as plt

def get_distance (point_1,point_2):
    return math.sqrt((point_1.x-point_2.x)**2+(point_1.y-point_2.y)**2)

class point:
    def __init__(self,position):
        self.x,self.y = position[0],position[1]

class plane:
    def __init__(self,min_separation,size):
        self.min_separation = min_separation
        self.size = size
        self.points = []

    def check_valid(self,new_point):
        valid = True
        for point in self.points:
            if get_distance(new_point,point) == self.min_separation:
                valid = False
                break
        return valid

    def create_point(self,position):
         new_point = point(position)
         if self.check_valid(new_point):
             self.points.append(new_point)

    def create_random_point(self):
        position = [random.randrange(self.size[0]),random.randrange(self.size[1])]
        self.create_point(position)

    def plot(self,point_size):
        x = []
        y = []
        for point in self.points:
            x.append(point.x)
            y.append(point.y)
        plt.scatter(x,y,s=point_size)
        plt.show()

distance = int(input("Distance: "))
x_size = int(input("X Size: "))
y_size = int(input("Y Size: "))
number_of_points = int(input("Number of points: "))
point_size = int(input("Point size: "))

plane = plane(distance,[x_size,y_size])
for i in range(number_of_points):
    plane.create_random_point()
plane.plot(point_size)
