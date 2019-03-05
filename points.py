import math
from random import shuffle
import matplotlib.pyplot as plt

def get_distance (point_1,point_2):
    return math.sqrt((point_1.x-point_2.x)**2+(point_1.y-point_2.y)**2)

def rotate_right(direction):
    new_direction = []
    if direction[0] == 1:
        new_direction = [0,-1]
    elif direction[1] == 1:
        new_direction = [1,0]
    elif direction[0] == -1:
        new_direction = [0,1]
    elif direction[1] == -1:
        new_direction = [-1,0]
    return new_direction

def move_direction(position,direction,n):
    new_position = [position[0] + direction[0] * n,position[1] + direction[1] * n]
    return new_position

def generate_real_spiral(size):
    current_position = [size[0]/2,size[1]/2]
    points = [current_position]
    n = 1
    direction = [0,1]
    while len(points) < size[0]*size[1]:
        for i in range(n):
            current_position = move_direction(current_position,direction,1)
            points.append(current_position)
        direction = rotate_right(direction)
        for i in range(n):
            current_position = move_direction(current_position,direction,1)
            points.append(current_position)
        direction = rotate_right(direction)
        n += 1
    for i in range(n-1):
        current_position = move_direction(current_position,direction,1)
        points.append(current_position)
    return points

def generate_spiral(size):
    points = [[0,0]]
    x = 0
    y = 0
    n = 1
    while len(points) < size[0]*size[1]:
        x += 1
        if not [x,y] in points:
            points.append([x,y])
        for i in range(n):
            y += 1
            if not [x,y] in points:
                points.append([x,y])
        while not x == 0:
            x -= 1
            if not [x,y] in points:
                points.append([x,y])
        y += 1
        if not [x,y] in points:
            points.append([x,y])
        n += 1
        for i in range(n):
            x += 1
            if not [x,y] in points:
                points.append([x,y])
        for i in range(n):
            y -= 1
            if not [x,y] in points:
                points.append([x,y])
        print("Loading",round(len(points)/(size[0]*size[1])*100),"%")
    return points

def generate_columns_upwards(size):
    points = []
    for i in range(size[0]):
        for e in range(size[1]):
            points.append([i,e])
            print("Loading",round(len(points)/(size[0]*size[1])*100),"%")
    return points

def generate_random(size):
    points = generate_columns_upwards(size)
    for i in range(10):
        shuffle(points)
    return points


class point:
    def __init__(self,position):
        self.x,self.y = position[0],position[1]

class plane:
    def __init__(self,min_separation,size):
        self.min_separation = min_separation
        self.size = size
        self.points = []
        self.points_raw = []

    def check_valid(self,new_point):
        valid = True
        for point in self.points:
            if get_distance(new_point,point) == self.min_separation:
                valid = False
                break
        return valid

    def create_point(self,position):
         new_point = point(position)
         if self.check_valid(new_point) and not [new_point.x,new_point.y] in self.points_raw:
             self.points.append(new_point)
             self.points_raw.append([new_point.x,new_point.y])

    def plot(self,point_size):
        x = []
        y = []
        for point in self.points:
            x.append(point.x/10)
            y.append(point.y/10)
        plt.scatter(x,y,s=point_size)
        plt.show()

if __name__ == "__main__":
    x_size = int(input("X size: "))*10
    y_size = int(input("Y size: "))*10
    size = [x_size,y_size]
    plane = plane(10,size)

    plot_type = str(input("Plot type (spiral/snake/columns/random): ")).lower()
    point_size = int(input("Plotted point size: "))
    if plot_type == "spiral":
        points = generate_real_spiral(size)
    if plot_type == "columns":
        points = generate_columns_upwards(size)
    if plot_type == "random":
        points = generate_random(size)
    if plot_type == "snake":
        points = generate_spiral(size)

    for index,position in enumerate(points):
        plane.create_point(position)
        print("Checked",round(index/len(points)*100),"%")
    print(len(plane.points),"points plotted")
    plane.plot(point_size)
